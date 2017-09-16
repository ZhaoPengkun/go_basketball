from flask_restplus import Namespace, Resource
from flask import request, jsonify
from app.api import api
from app.models.auth import User
from app.controllers.auth_controller import validate_email, query_user_info
from app.models.base import db
from log import logger
import schemas
import parameters

ns = Namespace('auth')


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
        new_user = User()
        new_user.email = email
        new_user.password = password
        validate_email_result = validate_email(email)
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


@ns.route('/login')
@api.doc(parser=parameters.login_parser)
class Auth(Resource):
    @ns.marshal_list_with(schemas.login)
    def post(self):
        """
        login in
        :return: login result
        :parameter: email, password
        """
        login_params = parameters.login_parser.parse_args()
        email = login_params.get('email')
        password = login_params.get("password")
        # return {"success": "test"}
        login_result = query_user_info(email, password)
        return login_result

# @ns.route('/')
# @api.doc(params={'taskid': 'task id'})
# class Task(Resource):
#     @ns.marshal_list_with(schemas.user_info)
#     def get(self):
#         task_id = request.args.get("task_id")
#         if task_id is None:
#             return None
#         else:
#             result = service.get_test_result(task_id)
#             return result
