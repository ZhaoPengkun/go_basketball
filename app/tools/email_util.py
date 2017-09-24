# -*- coding:UTF-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
from config import load_config

config = load_config()


# email_info = {"to_mail": "1443842506@qq.com", "subject": u"智能篮球验证码", "body": "I love you"}


def send_email(email_info):
    """
    send email
    :param email_info: {"to_mail": "1443842506@qq.com", "subject": u"智能篮球验证码", "body": "I love you"}
    :return:
    """

    # 初始化邮件
    encoding = 'utf-8'
    mail = MIMEText(email_info.get('body').encode(encoding), 'plain', encoding)
    mail['Subject'] = Header(email_info.get('subject'), encoding)
    mail['From'] = config.SMTP_USERNAME
    mail['To'] = email_info.get('to_mail')
    mail['Date'] = formatdate()

    try:

        # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
        smtp = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
        smtp.set_debuglevel(True)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)

        # 发送邮件
        smtp.sendmail(config.SMTP_USERNAME, email_info.get('to_mail'), mail.as_string())
        smtp.close()
        print 'OK'
    except Exception as e:
        print e


def send_verification_code_email(email, code):
    body = u"【智能篮球】您注册的智能篮球验证码为：" + code
    email_info = {"to_mail": email, "subject": u"智能篮球验证码", "body": body}
    send_email(email_info)

