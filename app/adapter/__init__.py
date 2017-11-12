from log import logger

from other import others


def init_module(app):
    _ = app
    logger.info("initialize adapter module")
    app.register_blueprint(others, url_prefix='/index')
