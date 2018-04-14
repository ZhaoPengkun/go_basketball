from flask_restplus.reqparse import RequestParser, Argument

email = RequestParser()
email.add_argument(Argument('email', required=True, type=str, help='please input email',
                            location='form'))
email.add_argument(Argument('order_id', required=True, type=str, help='please input order id',
                            location='form'))
