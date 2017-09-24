from flask_restplus.reqparse import RequestParser, Argument

register_parser = RequestParser()
register_parser.add_argument(Argument('email', required=True, type=str, help='please input email',
                                      location='form'))
register_parser.add_argument(Argument('password', required=True, type=str, help='please input password',
                                      location='form'))
register_parser.add_argument(Argument('code', required=True, type=str, help='please input verification code',
                                      location='form'))


login_parser = RequestParser()
login_parser.add_argument(Argument('email', required=True, type=str, help='please input email',
                                   location='form'))
login_parser.add_argument(Argument('password', required=True, type=str, help='please input password',
                                   location='form'))
