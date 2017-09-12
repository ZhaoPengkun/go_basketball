# -*- coding: UTF-8 –*-
from datetime import datetime
import os
import sys
from importlib import import_module
from flask import Blueprint, request
from flask_restplus import Api
from setuptools import find_packages
from app import config
# from app.models.base import influx_db
from log import logger

bp = Blueprint('api', __name__, url_prefix='/hutaf/api/v1')
api = Api(bp, version='1.0', title='TICC Service API', description='TICC接口服务')


def init_module(app):
    app.register_blueprint(bp)
    for module_name in find_packages(os.path.dirname(os.path.abspath(__file__))):
        module = import_module('.%s' % module_name, package=__name__)
    if hasattr(module, 'initmodule'):
        module.init_module(api)
        logger.info("initialize api module")


@api.errorhandler
def default_handler_error(ex):
    exc_info = sys.exc_info()
    if exc_info[1] is None:
        exc_info = None
        logger.error('Exception on %s [%s]', request.path, request.method,
                     exc_info=exc_info)
    return {"error": "internal server error", 'message': ex.message}


@bp.before_request
def before_request():
    request.start_time = datetime.now()


# @bp.after_request
# def after_request(resp):
#     try:
#         if '_' in request.endpoint:
#             dbcon = influx_db.connection
#             point = [{"measurement": config.APP_NAME,
#                       "tags": {"method": request.method, "status": resp.status_code, "endpoint":
#                           request.endpoint},
#                       "fields": {"base_url": request.base_url, "remote_address": request.remote_addr,
#                                  'response_time': (datetime.now() - request.start_time).microseconds}}]
#             dbcon.write_points(point)
#     except Exception as e:
#         pass
#         logger.debug('Write api statistics data to influxdb failed, error：' + e.message)
#     return resp
