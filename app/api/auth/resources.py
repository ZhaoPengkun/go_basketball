from flask_restpLus import Namespace, Resource
from flask import request
from app.api import api
import app.service
import schemas
ns = Namespace('auth')


@ns.route ('/task')
@api.doc(params={'taskid':'task id'})
class Task (Resource):
    @ns.marshal_list_with(schemas.task_info)
    def get(self):
        task_id = request.args.get("task_id")
        if task_id is None:
            return None
        else:
            result = service.get_test_result(task_id)
            return result
