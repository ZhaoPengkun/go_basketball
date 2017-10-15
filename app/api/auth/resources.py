# -*- coding:UTF-8 -*-
from flask_restplus import Namespace, Resource
from flask import request, session
from app.api import api
from app.models.auth import User
from app.controllers.auth_controller import validate_email, query_user_info, generate_verification_code
from app.models.base import db
from log import logger
import schemas
import parameters

ns = Namespace('auth')


@ns.route('/login')
class Auth(Resource):
    @api.doc(parser=parameters.login_parser)
    @ns.marshal_list_with(schemas.login)
    def post(self):
        """
        login in
        :return: {success, fail}
        :parameter: email, password
        """
        login_params = parameters.login_parser.parse_args()
        email = login_params.get('email')
        password = login_params.get("password")
        login_result = query_user_info(email, password)
        if login_result.get("login_result") == "success":
            session["email"] = email
        return login_result


@ns.route('/user_info')
@api.doc(parser=parameters.register_parser)
class UserInfo(Resource):
    @ns.marshal_list_with(schemas.register)
    def post(self):
        """
            register a user, write user info to database
            :parameter: username, password
            :return: register result ({success,double,illegal})
            """
        register_params = parameters.register_parser.parse_args()
        email = register_params.get('email')
        password = register_params.get("password")
        code = register_params.get("code")
        new_user = User()
        new_user.email = email
        new_user.password = password
        validate_email_result = validate_email(email, code)
        logger.info("validate email result:" + validate_email_result)
        try:
            if validate_email_result == "success":
                db.session.add(new_user)
                db.session.commit()
            result = {"register_result": validate_email_result}
            logger.info("register result:" + str(result))
        except Exception, e:
            logger.error("register fail error:", e)
            result = {"register_result": "fail"}
        return result


@ns.route('/')
@api.doc(params={"email": "please input email"})
class AuthEmail(Resource):
    @ns.marshal_list_with(schemas.verification)
    def get(self):
        """
        get email verification code
        :return: {"double":"email already exist", "success":"send email verification success"}
        """
        email = request.args.get('email')
        code = generate_verification_code(email)
        result = {"verification_code": code}
        return result
