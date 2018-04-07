#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'Duchengli'
# 淘股吧热帖爬虫V1
# 可以根据发布时间生成不同的文档
# 2018-04-07第三次创建

import requests
from bs4 import BeautifulSoup
import lxml
import os
import time

load_data = []
with open('淘股吧热帖存档.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        load_data.append(line[:-1])

#get_post_lists用于获取帖子列表，包括标题，发帖时间和帖子链接
def get_post_lists(page_number):
    time.sleep(2)
    page_url = 'https://www.taoguba.com.cn/index?pageNo=%d&blockID=1&flag=1' % page_number
    retry_time = 5
    for i in range(retry_time):
        try:
            r = requests.get(page_url,timeout=5)
            break
        except:
            if i < retry_time - 1:
                continue
            else:
                break

    if r.status_code == 200:
        print('第%d页爬取成功' %page_number)
        soup = BeautifulSoup(r.text, 'lxml')
        results = soup.find_all('li', class_='pcdj02')
        if results:
            for result in results:
                try:
                    post_title = result.a.text
                    post_date = result.parent.find('li',class_ = 'pcdj06').text
                    post_link = 'https://www.taoguba.com.cn/' + result.a.get('href')
                    likes = result.parent.find_all('li',class_ = 'pcdj05')
#tmp_str用于存储回帖/浏览/加油券三项数据
                    tmp_str = ''
                    for like in likes:
                        tmp_str = tmp_str + '/' + like.text
#                    print(post_title, post_date, post_link, tmp_str.split('/')[1], tmp_str.split('/')[2],tmp_str.split('/')[3])
                    if int(tmp_str.split('/')[1])>0 and int(tmp_str.split('/')[3])>0:#判断是否是热帖
                        if post_link in load_data:
                            pass
                        else:
                            print(post_title, post_date, post_link, tmp_str.split('/')[1], tmp_str.split('/')[2],tmp_str.split('/')[3])
                            load_data.append(post_link)
                except:
                    pass
    else:
        print('第%d页爬取失败' %page_number)

for i in range(1,20890):
#    print('正在分析第%d页' % i)
    get_post_lists(i)

#将改变后的load_data写回原来的文档,因为此时load_data不仅包括了新数据还包括了原来的数据，所用不能用a方法，只能用w方法
fobj=open("淘股吧热帖存档.txt",'w',encoding='utf-8')
fobj.writelines(str(items)+'\n' for items in load_data)
fobj.close()
