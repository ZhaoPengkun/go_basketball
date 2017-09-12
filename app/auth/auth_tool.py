# from app.models import User


def validate_email(email):
    """
    email must only one and is a email
    :param email:  email
    :return: {0:success,1:double email,2:not a email}
    """
    if User.query.filter_by(email=email).first():
        return "1"
    elif not_email(email):
        return "2"
    else:
        return "0"


def query_user_info(email, password):
    """
    login in
    :param email: login email
    :param password: login password
    :return: {0: success, 1: fail}
    """
    login_user = User.query.filter_by(email=email).first()
    if login_user:
        if login_user.verify_password(password):
            return "0"
    return "1"


def not_email(email):
    return False