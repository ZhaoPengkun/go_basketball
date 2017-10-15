from flask_restplus.reqparse import RequestParser, Argument

launch_challenge_parser = RequestParser()
launch_challenge_parser.add_argument(Argument('challenge_email', required=True, type=str, help="challenge's email",
                                              location='form'))
launch_challenge_parser.add_argument(Argument('be_challenge_email', required=True, type=str, help='be_challenge email',
                                              location='form'))
