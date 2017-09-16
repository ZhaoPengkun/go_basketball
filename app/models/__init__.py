from log import logger
from app.models.base import db


def init_module(app):
    db.init_app(app)
    logger.info("initialize model module")
