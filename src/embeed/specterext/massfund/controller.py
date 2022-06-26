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


@massfund_endpoint.route("/")
def index():
    return render_template(
        "massfund/index.jinja",
    )

