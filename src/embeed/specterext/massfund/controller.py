import logging
from flask import redirect, render_template, request, url_for, flash
from flask import current_app as app
from flask_login import login_required, current_user

from cryptoadvance.specter.specter import Specter
from cryptoadvance.specter.services.controller import user_secret_decrypted_required
from cryptoadvance.specter.user import User
from cryptoadvance.specter.wallet import Wallet
from cryptoadvance.specter.commands.psbt_creator import PsbtCreator
from .service import MassfundService
from .util import parse_csv

logger = logging.getLogger(__name__)

massfund_endpoint = MassfundService.blueprint

def ext() -> MassfundService:
    ''' convenience for getting the extension-object'''
    return app.specter.ext["massfund"]

def specter() -> Specter:
    ''' convenience for getting the specter-object'''
    return app.specter


@massfund_endpoint.route("/", methods=["GET", "POST"])
def index():
    user = app.specter.user_manager.get_user()
    show_menu = MassfundService.id in user.services

    wallet_names = sorted(current_user.wallet_manager.wallets.keys())
    wallets = [current_user.wallet_manager.wallets[name] for name in wallet_names]
    rawcsv = ""
    try:
        if request.method == "POST":
            action = request.form["action"]
            if action == "settings":
                show_menu = request.form.get("show_menu")
                if show_menu:
                    user.add_service(MassfundService.id)
                else:
                    user.remove_service(MassfundService.id)
            elif action == "parse":
                rawcsv = request.form.get("rawcsv", "")
                addresses, chain, invalid_lines = parse_csv(rawcsv)
                if chain != app.specter.chain:
                    raise ValueError(f"Invalid chain: {chain}, expected: {app.specter.chain}")
                # TODO: flash invalid_lines
                return render_template("massfund/table.jinja", wallets=wallets, addresses=addresses)
            # elif action == "createpsbt":
            #     wallet_alias = request.form.get("source_wallet")
                # wallet = current_user.wallet_manager.wallets[wallet_alias]
                # psbt_creator = PsbtCreator(
                #     app.specter,
                #     wallet,
                #     request.form.get("ui_option", "ui"),
                #     request_form=request.form,
                #     recipients_txt=request.form.get("recipients",""),
                #     recipients_amount_unit=request.form.get("amount_unit_text"),
                # )
                # psbt = psbt_creator.create_psbt(wallet)
                # return render_template(
                #     "wallet/send/sign/wallet_send_sign_psbt.jinja",
                #     psbt=psbt,
                #     labels=[""],
                #     wallet_alias=wallet_alias,
                #     wallet=wallet,
                #     specter=app.specter,
                #     rand=0,
                # )
            else:
                flash(f"Wrong action {action}", "error")
    except Exception as e:
        print(e)
        raise e
        flash(f"Server error: {e}", "error")
    return render_template(
        "massfund/index.jinja",
        wallets=wallets,
        show_menu=show_menu,
        rawcsv=rawcsv,
    )

