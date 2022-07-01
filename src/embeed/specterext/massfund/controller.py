import logging
from flask import redirect, render_template, request, url_for, flash
from flask import current_app as app
from flask_login import login_required, current_user

from cryptoadvance.specter.specter import Specter
from cryptoadvance.specter.services.controller import user_secret_decrypted_required
from cryptoadvance.specter.user import User
from cryptoadvance.specter.wallet import Wallet
from .service import MassfundService


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

    try:
        if request.method == "POST":
            action = request.form["action"]
            if action == "settings":
                show_menu = request.form.get("show_menu")
                if show_menu:
                    user.add_service(MassfundService.id)
                else:
                    user.remove_service(MassfundService.id)
            else:
                flash(f"Wrong action {action}", "error")
    except Exception as e:
        flash(f"Server error: {e}", "error")
    return render_template(
        "massfund/index.jinja",
        wallets=wallets,
        show_menu=show_menu
    )

