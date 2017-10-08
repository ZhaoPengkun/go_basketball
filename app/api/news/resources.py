# -*- coding:UTF-8 -*-
from app.tools.spider_util import start_spider

from flask_restplus import Namespace, Resource
from app.api import api
from flask import request
from log import logger
from app.models.base import db
from app.models.news import News
import schemas
import parameters

ns = Namespace('news')


@ns.route('/')
class New(Resource):
    @api.doc(parser=parameters.key_world_parser)
    def post(self):
        """
        spider web due to key word
        """
        key_world_parameters = parameters.key_world_parser.parse_args()
        key = key_world_parameters.get('key')
        logger.info("your spider key is " + key)
        start_spider(key)
        return {"result", "spider success"}

    def delete(self):
        """
        delete all news every day(3:00)
        """
        db.session.query(News).delete()


@api.doc(params={"page": "which page", "nums": "how much every page"})
@ns.route('/get_news')
class GetNews(Resource):
    @ns.marshal_list_with(schemas.mews)
    def get(self):
        page = int(request.args.get('page'))
        nums = int(request.args.get('nums'))
        news = db.session.query(News).filter().order_by(News.id.desc()).offset(page * (nums - 1)).limit(nums).all()
        result = []
        for new in news:
            result.append({"url": new.url, "pic": new.pic, "title": new.title})
        return result


