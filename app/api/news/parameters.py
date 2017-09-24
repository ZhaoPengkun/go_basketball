from flask_restplus.reqparse import RequestParser, Argument

news_parser = RequestParser()
news_parser.add_argument(Argument('page', required=True, type=int, help='which page',
                                  location='form'))
news_parser.add_argument(Argument('nums', required=True, type=int, help='how much every page',
                                  location='form'))

key_world_parser = RequestParser()
key_world_parser.add_argument(Argument('key', required=True, type=str, help='key word',
                                       location='form'))
