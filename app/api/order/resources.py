# -*- coding:UTF-8 -*-
from flask_restplus import Namespace, Resource
from flask import request, session
from app.api import api
from app.models import db
from app.models.order import Orders
import schemas
import parameters
ns = Namespace('order')


@ns.route('')
class Order(Resource):
    @api.doc(params={"email": "please input email"})
    @ns.marshal_list_with(schemas.order)
    def get(self):
        """
        get all order
        (need login)
        :return:
        """
        email = request.args.get('email')
        if "email" in session and session["email"] == email:
            orders = db.session.query(Orders).filter_by(email=email).all()
            order_list = []
            for order in orders:
                tmp_dict = {"email": order.email, "date": order.date, "status": order.status,
                            "price": order.price, "thing_info": order.thing_info, "order_id": order.id}
                order_list.append(tmp_dict)
            return order_list
        else:
            return {"result": False, "message": "please login in"}

    @api.doc(parser=parameters.email)
    @ns.marshal_list_with(schemas.result)
    def put(self):
        """
        delete a order (need login), just add a flag, not show
        :return: {success, fail}
        :parameter: email, password
        """
        order_params = parameters.email.parse_args()
        email = order_params.get('email')
        order_id = order_params.get("order_id")
        if "email" in session and session["email"] == email:
            order = db.session.query(Orders).filter_by(email=email, id=order_id).first()
            order.others = order.others + {"no_show": True}
            db.session.commit()
        else:
            return {"result": False, "message": "please login in"}
