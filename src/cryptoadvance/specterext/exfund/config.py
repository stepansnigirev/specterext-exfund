"""
Here Configuration of your Extension (and maybe your Application) takes place
"""
import os
from cryptoadvance.specter.config import ProductionConfig as SpecterProductionConfig


class BaseConfig:
    """This is a extension-based Config which is used as Base"""

    EXFUND_ASSETS_REGISTRY = {
        "liquidv1": "https://assets.blockstream.info/",
        "liquidtestnet": "https://assets-testnet.blockstream.info/"
    }


class ProductionConfig(BaseConfig):
    """This is a extension-based Config for Production"""

    pass


class AppProductionConfig(BaseConfig):
    """The AppProductionConfig class can be used to user this extension as application"""
    pass
    # # Where should the User endup if he hits the root of that domain?
    # ROOT_URL_REDIRECT = "/spc/ext/exfund"
    # # I guess this is the only extension which should be available?
    # EXTENSION_LIST = ["cryptoadvance.specterext.exfund.service"]
    # # You probably also want a different folder here
    # SPECTER_DATA_FOLDER = os.path.expanduser("~/.exfund")
