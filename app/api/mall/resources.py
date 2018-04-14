# -*- coding:UTF-8 -*-
from flask_restplus import Namespace, Resource
from app.api import api
import schemas
import parameters
from app.models.shopping_cart import ShoppingCarts
from app.models.shipping_address import ShippingAddresses
from flask import session, request
from app.models.base import db

ns = Namespace('mall')


@ns.route('/shopping_cart')
class ShoppingCart(Resource):
    @api.doc(parser=parameters.add_shopping_cart)
    @ns.marshal_list_with(schemas.modify)
    def post(self):
        """
        modify shopping cart
        thing_info: json format, {"thing_id":number}
        """
        shopping_cart_params = parameters.add_shopping_cart.parse_args()
        email = shopping_cart_params.get('email')
        thing_info = shopping_cart_params.get("thing_info")
        if "email" in session and session["email"] == email:
            new_shopping_cart = db.session.query(ShoppingCarts).filter_by(email=email).first()
            if not new_shopping_cart:
                new_shopping_cart = ShoppingCarts()
            new_shopping_cart.email = email
            new_shopping_cart.thing_info = thing_info
            db.session.add(new_shopping_cart)
            db.session.commit()
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "please login in"}

    @api.doc(params={"email": "please input email"})
    @ns.marshal_list_with(schemas.modify)
    def get(self):
        """
        get shopping cart thing info
        (need login)
        :return:
        """
        # email_param = parameters.email_params.parse_args()
        email = request.args.get('email')
        if "email" in session and session["email"] == email:
            new_shopping_cart = db.session.query(ShoppingCarts).filter_by(email=email).first()
            if new_shopping_cart:
                return {"result": True, "message": new_shopping_cart.thing_info}
        else:
            return {"result": False, "message": "please login in"}


@ns.route('/shipping_address')
class ShippingAddress(Resource):
    @api.doc(parser=parameters.add_shipping_address)
    @ns.marshal_list_with(schemas.modify)
    def post(self):
        """
        modify shipping address
        thing_info: json format, {"thing_id":number}
        """
        shipping_address_params = parameters.add_shipping_address.parse_args()
        email = shipping_address_params.get('email')
        address_info = shipping_address_params.get("address_info")
        if "email" in session and session["email"] == email:
            new_shipping_address = db.session.query(ShippingAddresses).filter_by(email=email).first()
            if not new_shipping_address:
                new_shipping_address = ShippingAddresses()
            new_shipping_address.email = email
            new_shipping_address.address_info = address_info
            db.session.add(new_shipping_address)
            db.session.commit()
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "please login in"}

    @api.doc(params={"email": "please input email"})
    @ns.marshal_list_with(schemas.modify)
    def get(self):
        """
        get shipping address
        (need login)
        :return:
        """
        email = request.args.get('email')
        if "email" in session and session["email"] == email:
            new_shipping_address = db.session.query(ShippingAddresses).filter_by(email=email).first()
            if new_shipping_address:
                return {"result": True, "message": new_shipping_address.address_info}
        else:
            return {"result": False, "message": "please login in"}
