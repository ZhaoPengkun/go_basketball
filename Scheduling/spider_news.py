# -*- coding:UTF-8 -*-
import requests


def start(spider_url):
    requests.post(spider_url, data={"key": u"篮球"})


if __name__ == "__main__":
    url = "http://localhost:8088/api/v1/news/"
    start(url)
