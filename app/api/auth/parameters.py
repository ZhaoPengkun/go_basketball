from flask_restplus.reqparse import RequestParser, Argument

register_parser = RequestParser()
register_parser.add_argument(Argument('email', required=True, type=str, help='please input email',
                                      location='form'))
register_parser.add_argument(Argument('password', required=True, type=str, help='please input password',
                                      location='form'))

login_parser = register_parser
# login_parser.add_argument(Argument('email', required=True, type=str, help='please input email',
#                                    location='form'))
# login_parser.add_argument(Argument('password', required=True, type=str, help='please input password',
#                                    location='form'))
