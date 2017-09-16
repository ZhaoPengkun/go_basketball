import re
from app.models.auth import User


def validate_email(email):
    """
    email must only one and is a email
    :param email:  email
    :return: {0:success,1:double email,2:illegal}
    """
    if not_email(email):
        return "illegal"
    elif User.query.filter_by(email=email).first():
        return "double"
    else:
        return "success"


def query_user_info(email, password):
    """
    login in
    :param email: login email
    :param password: login password
    :return: {success, fail}
    """
    login_user = User.query.filter_by(email=email).first()
    if login_user:
        if login_user.verify_password(password):
            print "verify"
            return {"login_result": "success"}
    return {"login_result": "fail"}


def not_email(email):
    if len(email) > 7:
        if re.match("^.+@(\\[?)[a-zA-Z0-9\\-.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return False
    return True
