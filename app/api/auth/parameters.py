from flask_restplus.reqparse import RequestParser, Argument
from werkzeug.datastructures import FileStorage

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

modify_parser = RequestParser()
modify_parser.add_argument(Argument('email', required=True, type=str, help='please input email',
                                    location='form'))
modify_parser.add_argument(Argument('password', required=False, type=str, help='please input password',
                                    location='form'))
modify_parser.add_argument(Argument('username', required=False, type=str, help='please input username',
                                    location='form'))
modify_parser.add_argument(Argument('phone', required=False, type=str, help='please input phone',
                                    location='form'))
modify_parser.add_argument(Argument('address', required=False, type=str, help='please input address',
                                    location='form'))
modify_parser.add_argument(Argument('height', required=False, type=str, help='please input height',
                                    location='form'))
modify_parser.add_argument(Argument('weight', required=False, type=str, help='please input weight',
                                    location='form'))
modify_parser.add_argument(Argument('vip', required=False, type=str, help='please input vip days',
                                    location='form'))
modify_parser.add_argument(Argument('step_number', required=False, type=str, help='please input step number',
                                    location='form'))
modify_parser.add_argument(Argument('portrait', required=False, type=FileStorage, help='please input portrait',
                                    location='files'))
modify_parser.add_argument(Argument('bust', required=False, type=str, help='please input bust',
                                    location='form'))
modify_parser.add_argument(Argument('Waist', required=False, type=str, help='please input Waist',
                                    location='form'))
modify_parser.add_argument(Argument('BMI', required=False, type=str, help='please input BMI',
                                    location='form'))
