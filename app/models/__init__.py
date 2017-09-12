from log import logger
from app.models.base import influx_db


def init_module(app):
    # influx_db.init_app(app)
    logger.info("initialize model module")
