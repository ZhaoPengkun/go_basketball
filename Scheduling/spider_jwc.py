# -*- coding:UTF-8 -*-
import urllib2
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def parse(page, xpath):
    url_div = page.xpath(xpath)
    return url_div


def get_page(url, headers):
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    return etree.HTML(html.decode('utf-8'))


def jwc_start_spider():
    url = 'http://jwc.scu.edu.cn/jwc/frontPage.action'
    headers = {'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'",
                'Host': 'jwc.scu.edu.cn',
               'Pragma': 'no-cache',
               'Upgrade-Insecure-Requests': '1',
               'Cookie': 'JSESSIONID=93F496D7F5AA8236C66E8439C3A43D9F; JSESSIONID=5DA2FDFB4A517ED2D4BF231FF5047DAE',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Mobile Safari/537.36',
               'Referer': 'http://jwc.scu.edu.cn/'}
    page = get_page(url, headers)
    result = {}
    trs = parse(page, '//*[@class="STYLE4"]/a')
    # for tr in trs:
    #     result = 0
    for tr in trs:
        name = tr.find("span").text
        url = tr.get("href")
        result[name] = "http://jwc.scu.edu.cn/jwc/" + url
    return result


if __name__ == "__main__":
    jwc_start_spider()
