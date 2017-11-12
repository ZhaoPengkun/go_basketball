# -*- coding:UTF-8 -*-
import urllib2
from lxml import etree
import sys
from app.models.base import db
from app.models.video import Video
import time

reload(sys)
sys.setdefaultencoding('utf8')

host = "http://mp.weixin.qq.com"


def parse(page, xpath):
    url_div = page.xpath(xpath)
    return url_div


def get_page(url, headers):
    req = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(req)
    html = page.read()
    return etree.HTML(html.decode('utf-8'))


def get_info(url, headers):
    page = get_page(url, headers)

    for i in range(1, 2):
        video = Video()
        a_tag = parse(page, '//*[@id="result_list"]/li['+str(i)+']/a')[0]
        image_tag = parse(page, '//*[@id="result_list"]/li['+str(i)+']/a/img/@src')
        tmp_title = parse(page, '//*[@id="result_list"]/li['+str(i)+']/a/img/@title')
        tmp_href = str(a_tag.get("href"))
        tmp_url2 = tmp_href.split("-")[1][0:-5]
        url2 = "http://me.cztv.com/wap/play?id=" + tmp_url2
        url2_headers = {'Host': 'me.cztv.com',
                   'Pragma': 'no-cache',
                   'Upgrade-Insecure-Requests': '1',
                   'Cookie': 'acw_tc=AQAAAMkKxgCyeA0AAWtFfX0XQQv4543+; Hm_lvt_ebf8a8028c76b35add2bcc96bdb8ac4a=1510231773; Hm_lpvt_ebf8a8028c76b35add2bcc96bdb8ac4a=1510231773; UM_distinctid=15fa0d40f276bb-0429ee49497c6f-7b1f3c-100200-15fa0d40f28abb; CNZZDATA1253108499=1590061719-1510229071-null%7C1510229071; CNZZDATA4090300=cnzz_eid%3D426104111-1510228162-%26ntime%3D1510231061',
                   'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Mobile Safari/537.36',
                   'Referer': 'http://me.cztv.com' + tmp_href}

        page2 = get_page(url2, url2_headers)
        mp4_src = parse(page2, '//*[@id="player"]/@src')
        video.name = str(tmp_title)
        video.url = mp4_src[0]
        video.image_src = image_tag[0]
        db.session.add(video)
        db.session.commit()
        time.sleep(20)


def mp4_start_spider():
    url = 'http://me.cztv.com/search/list/page/1/keyword/%E7%AF%AE%E7%90%83'
    headers = {'Host': 'me.cztv.com',
               'Pragma': 'no-cache',
               'Upgrade-Insecure-Requests': '1',
               'Cookie': 'UM_distinctid=15f77c8e618a64-0140d6cddb841e-28782141-57f72-15f77c8e6195a5; acw_tc=AQAAAOkrtGkuZwgAHuZydkFdB2sYihkN; _gscu_1136605835=09548394sor90020; _gscs_1136605835=09548394xlix3o20|pv:1; _gscbrs_1136605835=1; CNZZDATA5191113=cnzz_eid%3D627395367-1509543130-http%253A%252F%252Fwww.cztv.com%252F%26ntime%3D1509543130; Hm_lvt_ebf8a8028c76b35add2bcc96bdb8ac4a=1509545496,1509545556,1509547005,1509547952; Hm_lpvt_ebf8a8028c76b35add2bcc96bdb8ac4a=1509548455; CNZZDATA4090300=cnzz_eid%3D1732855090-1509547551-http%253A%252F%252Fwww.cztv.com%252F%26ntime%3D1509547551',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Mobile Safari/537.36',
               'Referer': 'http://me.cztv.com/search/list/page/2/keyword/%E7%AF%AE%E7%90%83'}

    get_info(url, headers)
    return "spider success"


