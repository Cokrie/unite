#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
import re
import threading
import requests
#test django
from django.http import HttpResponse


#Global Variable
global URL_LIST
global REGULAR_EXPRESSION

URL_LIST = {'baidu_url': 'http://www.baidu.com/s?wd=%s&pn=%s',
            'baidu_tieba_url': 'http://tieba.baidu.com/f?ie=utf-8&kw=%s&pn=%s',
            'weibo_url': 'http://s.weibo.com/weibo/%s&Refer=focus_lx_STopic_box'}

REGULAR_EXPRESSION = {'baidu_url': 'div.result h3.t > a',
            'baidu_tieba_url': 'a.j_th_tit',
            'weibo_url': 'p.comment_txt'}


def requests_test():

    res = requests.get('http://jandan.net/ooxx')
    html = BeautifulSoup(res.text)
    for index, each in enumerate(html.select('#comments img')):
        with open('{}.jpg'.format(index), 'wb') as jpg:
            jpg.write(requests.get(each.attrs['src'], stream=True).content)


def baidu_spider(page_num):

    #with open('/opt/baidu_result.txt','wa') as f:

    #with open('./keyword.txt','r') as keywords:

    for url_name in get_url_list():

        if url_name == "baidu_tieba_url":
            tmp = '_tieba.txt'
        else:
            tmp = '.txt'
        keywords = open('./keyword/keyword' + tmp, 'r')
        with open(('/opt/spider/%s' % url_name)[:-4] + '.txt', 'wa') as f:
            for keyword in keywords:

                f.writelines('--------------------------------------------------------------\n')
                f.writelines('the keyword is '+keyword+'\n')
                page = 1
                while page <= int(page_num):

                    #page_now = str((int(page) - 1) * 10)

                    #url = 'http://www.baidu.com/s?wd='+urllib.quote(keyword.strip().decode(sys.stdin.encoding).encode('gbk'))+'&pn='+str(page_now)
                    url = URL_LIST[url_name] % (str(keyword).strip(), get_page(url_name, page))
                    request = urllib2.Request(url)
                    response = urllib2.urlopen(request)

                    soup = BeautifulSoup(response.read())

                    data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select(REGULAR_EXPRESSION[url_name])]

                    for item in data:
                        f.writelines(''.join(item.strip().split())+'\n')

                    page = int(page) + 1



    '''
    weibo
    '''

    keywords = open('./keyword/keyword_weibo.txt', 'r')
    with open('/opt/spider/weibo.txt', 'wa') as f:
        for keyword in keywords:

            f.writelines('--------------------------------------------------------------\n')
            f.writelines('the keyword is '+keyword+'\n')
            url = URL_LIST['weibo_url'] % (str(keyword).strip())
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)

            soup = BeautifulSoup(response.read())

            data = [re.sub(u'<[\d\D]*?>',' ',str(item)) for item in soup.select(REGULAR_EXPRESSION['weibo_url'])]

            for item in data:
                f.writelines(''.join(item.strip().split())+'\n')


    print 'over'


def get_url_list():

    url_list = ['baidu_url',
                'baidu_tieba_url'
                ]
    return url_list;


def get_page(url_name, page):

    page = {
        'baidu_url': str((int(page) - 1) * 10),
        'baidu_tieba_url': str((int(page) - 1) * 50)
    }
    return page.get(url_name)


def django_web():

    return HttpResponse()


def timer(page_num):

    '''
    once per 3 minutes
    :return:
    '''
    #baidu_spider(page_num)
    t = threading.Timer(20, baidu_spider(page_num))
    t.start()


def sys_exit():

    sys.exit()


if __name__ == "__main__":

    page_num = str(input(u'Please input the page number：\n'))
    t = timer(page_num)
    #while True:
        #None
