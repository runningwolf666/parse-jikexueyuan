#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

import time
import requests  # 快速上手： http://cn.python-requests.org/zh_CN/latest/user/quickstart.html 本页内容为如何入门Requests提供了很好的指引。
from lxml import html

def parseJkxy(url):
    headers = {
        # GET /course/?pageNum=5 HTTP/1.1
        'Host': 'www.jikexueyuan.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.jikexueyuan.com/course/'
    }

    r = requests.get(url, headers=headers)
    print('status_code: {}  url: {}'.format(r.status_code, url))
    r.encoding = 'utf-8'
    doc = html.document_fromstring(r.text)

    # Save the related information
    titles_, intros_, courses_, numbers_, levels_ = [], [], [], [], []

    # title
    # html body div#wrapper div#pager div#container.asideL div.wrap.w-1000.mar-t20 div#main div.tagGather div.bd div.listbox div#changeid.lesson-list ul.cf li#1680 div.lesson-infor h2.lesson-info-h2 a
    titles = doc.cssselect('ul.cf li div.lesson-infor h2.lesson-info-h2 a')
    for title in titles:
        titles_.append(title.text_content())

    # introduction
    # html body div#wrapper div#pager div#container.asideL div.wrap.w-1000.mar-t20 div#main div.tagGather div.bd div.listbox div#changeid.lesson-list ul.cf li#1680 div.lesson-infor p
    intros = doc.cssselect('ul.cf li div.lesson-infor p')
    for intro in intros:
        intros_.append( intro.text_content().replace('\n', ' ').replace('\t', '') )

    # course time
    # html body div#wrapper div#pager div#container.asideL div.wrap.w-1000.mar-t20 div#main div.tagGather div.bd div.listbox div#changeid.lesson-list ul.cf li#1680 div.lesson-infor div.timeandicon div.cf dl dd.mar-b8 em
    courses = doc.cssselect('ul.cf li div.lesson-infor div.timeandicon div.cf dl dd.mar-b8 em')
    for course in courses:
        courses_.append( course.text_content().replace('\n', ' ').replace('\t', '') )

    # learn number
    # html body div#wrapper div#pager div#container.asideL div.wrap.w-1000.mar-t20 div#main div.tagGather div.bd div.listbox div#changeid.lesson-list ul.cf li#1680 div.lesson-infor div.timeandicon div.cf em.learn-number
    numbers = doc.cssselect('ul.cf li div.lesson-infor div.timeandicon div.cf em.learn-number')
    for number in numbers:
        numbers_.append(number.text_content())

    # level
    # html body div#wrapper div#pager div#container.asideL div.wrap.w-1000.mar-t20 div#main div.tagGather div.bd div.listbox div#changeid.lesson-list ul.cf li#1680 div.lesson-infor div.timeandicon div.cf dl dd.zhongji em
    levels = doc.cssselect('ul.cf li div.lesson-infor div.timeandicon div.cf dl dd.zhongji em')
    for level in levels:
        levels_.append(level.text_content())

    # write to .txt file
    for i in range(len(titles_)):
        with open(txtname, 'a') as f:
            f.writelines('title: ' + titles_[i] + '\n')
            f.writelines('classinfo: ' + intros_[i] + '\n')
            f.writelines('classtime: ' + courses_[i] + '\n')
            f.writelines('learn_number: ' + numbers_[i] + '\n')
            f.writelines('class_level: ' + levels_[i] + '\n\n')


timestyle = time.strftime('%H%M%S')
txtname = 'jkxy-{}.txt'.format(timestyle)
for i in range(2,5):
    url = 'http://www.jikexueyuan.com/course/?pageNum={}'.format(i)
    parseJkxy(url)
    time.sleep(0.5)



