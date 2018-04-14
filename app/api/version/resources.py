# -*- coding:UTF-8 -*-
from flask_restplus import Namespace, Resource
from config import load_config
from flask import send_from_directory, make_response
import os
config = load_config()

ns = Namespace('version')


@ns.route('/get_now_version_id')
class Version(Resource):
    def get(self):
        """
        get now version id
        :return:
        """
        return {"version_id": config.version_id}


@ns.route('/download_newest_app')
class Download(Resource):
    def get(self):
        """
        download newest app
        :return:
        """
        # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
        directory = os.getcwd()
        response = make_response(send_from_directory(directory, config.app_name, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(config.app_name.encode().decode('latin-1'))
        return response
