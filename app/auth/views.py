# -*- coding: UTF-8 –*-
from . import auth
from flask import request
from auth_tool import validate_email, query_user_info
from app.models import User
from ..__init__ import db


@auth.route('/login', methods=['Post'])
def login():
    """
    login in
    :return: login result
    :parameter: email, password
    """
    email = request.args.get("email")
    password = request.args.get("password")
    login_result = query_user_info(email, password)
    return login_result


@auth.route('/register', methods=['Post'])
def register():
    """
    register a user, write user info to database
    :parameter: username, password
    :return: register result (detail in auth_tool.py)
    """
    email = request.args.get("email")
    password = request.args.get("password")
    new_user = User()
    new_user.email = email
    new_user.password = password
    validate_email_result = validate_email(email)
    print validate_email_result
    if validate_email_result == "0":
        db.session.add(new_user)
        db.session.commit()
        return validate_email_result
    else:
        return validate_email_result
    # pass
