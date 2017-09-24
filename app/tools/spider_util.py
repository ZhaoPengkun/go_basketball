# -*- coding:UTF-8 -*-
import urllib2
from lxml import etree
import sys
import time
from app.models.base import db
from app.models.news import News
reload(sys)
sys.setdefaultencoding('utf8')

host = "http://mp.weixin.qq.com"


def parse(page, xpath):
    url_div = page.xpath(xpath)
    return url_div


def get_page(url, headers, key_value):
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    html = html.replace(u"<em><!--red_beg-->"+key_value+"<!--red_end--></em>", key_value)
    return etree.HTML(html.decode('utf-8'))


def get_info(url, headers, key_value):
    page = get_page(url, headers, key_value)

    for i in range(0, 10):
        new = News()
        url = parse(page, '//*[@id="sogou_vr_11002601_title_' + str(i) + '"]/@href')
        new.url = url[0]
        text_tmp = parse(page, '//*[@id="sogou_vr_11002601_title_' + str(i) + '"]')
        pic = parse(page, '//*[@id="sogou_vr_11002601_img_' + str(i) + '"]/img/@src')
        if not pic:
            pic = parse(page, '//*[@id="sogou_vr_11002601_img_' + str(i) + '_1"]/span/img/@src')
        new.title = str(text_tmp[0].text)
        new.pic = pic[0]
        db.session.add(new)
        db.session.commit()


def start_spider(key_value):
    url = 'http://weixin.sogou.com/weixin?type=2&query='+key_value+'&ie=utf8'
    headers = {'Host': 'weixin.sogou.com',
               'Pragma': 'no-cache',
               'Upgrade-Insecure-Requests': '1',
               'Cookie': 'ABTEST=0|1505736750|v1; IPLOC=CN5101; SUID=CA6B457D2423910A0000000059BFB82E; SUID=CA6B457D4F18910A0000000059BFB82E; weixinIndexVisited=1; SUV=006317867D456BCA59BFB83040B89926; SNUID=E4DD36E18F8AD73C02C01B5B8F5E5DEF; sct=24; JSESSIONID=aaaEj-KY0sAvL_oKE2y6v',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Mobile Safari/537.36'}
    for i in range(1, 11):
        tmp_url = "http://weixin.sogou.com/weixin?query=%E7%AF%AE%E7%90%83&_sug_type_=&sut=5519&lkt=1%2C1506244505656%2C1506244505656&s_from=input&_sug_=y&type=2&sst0=1506244505757&page="+str(i)+"&ie=utf8&w=01019900&dr=1"
        # tmp_url = url + "&page="+str(i)
        print tmp_url
        get_info(tmp_url, headers, key_value)
        time.sleep(60)
    return "spider success"


if __name__ == "__main__":
    start_spider()
