# -*- coding: utf-8 -*-
import json
import logging.handlers
import time
import os
import socket
import sys
import requests
from config import *

config = load_config()


def record_json_msg(record):
    try:
        properties = [item for item in dir(record) if not item.startswith("_")]
        record_dict = {item: getattr(record, item) for item in properties if
                       item not in ["args", "getMessage", "message"]}
        return record_dict
    except:
        raise


def get_local_ip():
    try:
        c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        c_sock.connect(('8.8.8.8', 80))
        (address, port) = c_sock.getsockname()
        c_sock.close()
        if "172.17" in address:
            address = config.SERVER_HOST
        return address
    except socket.error:
        try:
            socket.getfqdn(socket.gethostname())
        except:
            return "127.0.0.1"


def http_post(url, data):
    jd = json.dumps(data)
    req = requests.post(url, data=jd, timeout=10.0)
    return req.ok


class ElasticHandler(logging.Handler):
    def __init__(self, index, port, elastic_url, elastic_type="log"):
        logging.Handler.__init__(self)
        self.elastic_url = elastic_url
        mode = os.environ.get('MODE', "testing").lower()
        self.index = "{}_{}_{}".format(index, mode, port)
        self.type = elastic_type
        mapping = {"mappings": {self.type: {"properties": {"@timestamp": {"type":"date"}}}}}
        try:
            jd = json.dumps(mapping)
            requests.put("%s/%s" %(self.elastic_url, self.index), data=jd, timeout=10.0)
        except:
            pass

    def emit(self, record):
        url = "%s/%s/%s" % (self.elastic_url, self.index, self.type)
        try:
            data = record_json_msg(record)
            data["@timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
            data["source"] = get_local_ip()
            http_post(url, data)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            pass
if not os.path.exists('logs'):
    os.mkdir('logs')
formatter = logging.Formatter('[%(asctime)s]<pid=%(process)d tid=%(thread)d>%(levelname)s - %(message)s')
file_handler = logging.handlers.RotatingFileHandler("logs/cte.log", maxBytes=20 * 1024 * 1024, backupCount=25)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# elk_handler = ElasticHandler(config.APP_NAME, config.PORT, config.ELASTIC_URI)
# elk_handler.setFormatter(formatter)
# elk_handler.setLevel(logging.DEBUG)

error_handler = logging.handlers.RotatingFileHandler("logs/cte_error.log", maxBytes=20 * 1024*1024,backupCount=25)
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)

# create logger
logger = logging.getLogger('fLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# logger.addHandler(elk_handler)
logger.addHandler(error_handler)
