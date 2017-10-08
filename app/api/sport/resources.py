# -*- coding:UTF-8 -*-

from flask_restplus import Namespace, Resource
from app.api import api
from flask import request, Response
from log import logger
from app.models.base import db
from app.models.auth import User
from app.models.challenger_info import ChallengerInfo
import schemas
import time

ns = Namespace('sport')


@api.doc(params={"email": "user's email"})
@ns.route('/')
class GameInfo(Resource):
    @ns.marshal_list_with(schemas.game_info)
    def get(self):
        time_stmp = time.localtime(time.time())
        now_date = time.strftime('%A/%m/%d/%Y', time_stmp)
        now_time = time.strftime('%H', time_stmp)
        result = {"date": now_date, "time": now_time}
        email = request.args.get('email')
        logger.error("get sport game info by email:" + email)
        vip = db.session.query(User.vip).filter_by(email=email).first()
        result["challenger"] = db.session.query(ChallengerInfo.be_challenger).filter_by(challenger=email)
        result["be_challenger"] = db.session.query(ChallengerInfo.challenger).filter_by(be_challenger=email)
        result["vip"] = vip[0]
        return result



@api.doc(params={"i": "top i. eg:top 1 will return top1's head portrait"})
@ns.route('/get_top_image')
class ImageTop(Resource):
    def get(self):
        i = int(request.args.get('i'))
        print str(i)
        if i > 3:
            result = {"error": "not support i > 3"}
            return result

        logger.info("get top %d from db" % i)
        user = db.session.query(User).filter().order_by(User.step_number.desc()).offset(i - 1).first()
        respon = Response(user.portrait, mimetype="image/jpeg")
        return respon
