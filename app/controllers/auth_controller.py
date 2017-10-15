import re
import random
from app.models.auth import User, Auth
from app.models.base import db
from app.tools.email_util import send_verification_code_email


def validate_email(email, code):
    """
    email must only one and is a email
    :param email:  email
    :return: {0:success,1:double email,2:illegal}
    """
    auth = Auth()
    auth.verification_code = code
    auth.email = email
    if not_email(email):
        return "illegal"
    elif db.session.query(User).filter_by(email=email).first():
        return "double"
    else:
        auth = db.session.query(Auth).filter_by(email=email).first()
        if auth.verification_code == code:
            db.session.delete(auth)
            return "success"
        else:
            return "verification error"
        # print email
        # # user = session.query(User).filter_by(username='abc').first()
        # # session.delete(user)
        # if Auth.query.filter_by(email=email).first():
        #     db.session.delete(auth)
        #     db.session.commit()
        #     return "success"
        # else:
        #     return "verification error"


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


def generate_verification_code(email):
    if User.query.filter_by(email=email).first():
        return "double"
    code = str(random.randint(0, 99999999)).zfill(8)
    auth = Auth()
    auth.email = email
    auth.verification_code = code
    if Auth.query.filter_by(email=email).first():
        db.session.query(Auth).filter(Auth.email == email).update({"verification_code":code})
    else:
        db.session.add(auth)
    db.session.commit()
    send_verification_code_email(email, code)
    return "success"
