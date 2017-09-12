from flask_restplus.reqparse import RequestParser, Argument

task_post = RequestParser()
task_post.add_argument(Argument('params',
                                required=True, type=str, help='Task	Crater',
                                location='form'))
