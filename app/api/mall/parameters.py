from flask_restplus.reqparse import RequestParser, Argument

add_shopping_cart = RequestParser()
add_shopping_cart.add_argument(Argument('email', required=True, type=str, help='please input email',
                                        location='form'))
add_shopping_cart.add_argument(Argument('thing_info', type=str, help='the format is "json"',
                                        location='form'))

add_shipping_address = RequestParser()
add_shipping_address.add_argument(Argument('email', required=True, type=str, help='please input email',
                                           location='form'))
add_shipping_address.add_argument(Argument('address_info', type=str, help='the format is "json"',
                                           location='form'))

email_params = RequestParser()
email_params.add_argument(Argument('email', required=True, type=str, help='please input email',
                                   location='form'))
