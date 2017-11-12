from flask import Blueprint, render_template, send_from_directory

others = Blueprint("index", __name__)


@others.route('')
def index():
    # return send_from_directory("app/templates/theme", "index.html")
    return render_template("index.html")


@others.route('/download')
def download():
    print "inddex"
    # return send_from_directory("app/templates/theme", "index.html")
    return render_template("download.html")


