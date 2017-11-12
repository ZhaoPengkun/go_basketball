# -*- coding:UTF-8 -*-

from flask_restplus import Namespace, Resource
from app.api import api
from flask import request, Response, session
from log import logger
from app.models.base import db
from app.models.auth import User
from app.models.challenger_info import ChallengerInfo
import schemas
import time
import parameters

ns = Namespace('sport')


@ns.route('/')
class GameInfo(Resource):
    @api.doc(params={"email": "user's email"})
    @ns.marshal_list_with(schemas.game_info)
    def get(self):
        """
        get game info
        :return: game info
        """
        # if "email" in session and session["email"]
        time_stmp = time.localtime(time.time())
        now_date = time.strftime('%A/%m/%d/%Y', time_stmp)
        now_time = time.strftime('%H', time_stmp)
        result = {"date": now_date, "time": now_time}
        email = request.args.get('email')
        logger.error("get sport game info by email:" + email)
        vip = db.session.query(User.vip).filter_by(email=email).first()
        challenger = db.session.query(ChallengerInfo.be_challenger).filter_by(challenger=email)
        tmp_challenger = []

        for i in challenger:
            tmp = db.session.query(User.username).filter_by(email=str(i[0]))
            tmp_challenger.append(tmp[0])
        result["challenger"] = tmp_challenger
        tmp_be_challenger = []
        be_challenger = db.session.query(ChallengerInfo.challenger).filter_by(be_challenger=email)
        for j in be_challenger:
            tmp = db.session.query(User.username).filter_by(email=str(j[0]))
            tmp_be_challenger.append(tmp[0])
        result["be_challenger"] = tmp_be_challenger
        result["vip"] = vip[0]
        return result

    @api.doc(parser=parameters.launch_challenge_parser)
    def post(self):
        """
        launch a challenge
        :return:
        """
        launch_challenge_params = parameters.launch_challenge_parser.parse_args()
        challenge_email = launch_challenge_params.get('challenge_email')
        be_challenge_email = launch_challenge_params.get('be_challenge_email')
        if "email" in session and session["email"] == challenge_email:
            if not db.session.query(User).filter_by(email=be_challenge_email).first():
                return {"result": "error", "message": "be_challenge_email not exist"}
            new_challener = ChallengerInfo()
            new_challener.challenger = challenge_email
            new_challener.be_challenger = be_challenge_email
            try:
                db.session.add(new_challener)
                return {"result": "success"}
            except Exception as e:
                logger.error("launch a challenge error:" + str(e))
                return {"result": "error", "message": str(e)}
        else:
            return {"result": "error", "message": "please login"}


@api.doc(params={"i": "top i. eg:top 1 will return top1's head portrait"})
@ns.route('/get_top_image')
class ImageTop(Resource):
    def get(self):
        i = int(request.args.get('i'))
        if i > 3:
            result = {"error": "not support i > 3"}
            return result

        logger.info("get top %d from db" % i)
        user = db.session.query(User).filter().order_by(User.step_number.desc()).offset(i - 1).first()
        respon = Response(user.portrait, mimetype="image/jpeg")
        return respon
