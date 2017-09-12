import pkgutil
import os
from importlib import import_module
from flask import Flask as _Flask
from flask_cors import CORS
from config import load_config

config = load_config()


class Flask(_Flask):
    def __init__(self, name, cfg):
        super(Flask, self).__init__(name, instance_relative_config=True)
        self.config.from_object(cfg)
        CORS(self)


def _init_module(app):
    # pylint:disable=unused-variable
    for importer, modname, ispkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
        if ispkg:
            mod = import_module('.%s' % modname, package=__name__)
            if hasattr(mod, 'init_module'):
                mod.init_module(app)


def create_app():
    app = Flask(__name__, cfg=config)
    # pylint: disable=attribute-defined-outside-init
    _init_module(app)
    return app
