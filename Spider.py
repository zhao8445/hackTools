# -*- coding: utf-8 -*-
import requests
import sys
import threading
from bs4 import BeautifulSoup
import json
import Queue
import bs4

url = 'https://www.lagou.com/'
headers = {}
links = set()

class spider(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not self.queue.empty():
            num = self.queue.get()
            self.exec_spider(num)

    def exec_spider(self):
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.content)
        a = soup.find_all('a')
        for i in range(len(a)):
            print a[i]

    # 判断空链接与不符合条件的结果
    def links_check(self,link):
        if link != '#' and link != '' and '(' not in link:
            self.link_parse(link)

    # 对获得的链接进行补全
    def link_parse(self,r_link):
        if '://' in r_link:
            links.add(r_link)
        if '://' not in r_link:
            r_link = 'http://10.1.1.155' + r_link
            links.add(r_link)
        return links

    def url_parse(self,url):
        if 'http' in url:
            try:
                self.get_href(url)
            except:
                print u'所输入的地址有误或无法访问，请检查----'
                print u'请输入这种格式：http://xxx.xxx.xx 或者 https://xxx.xxx.xx'
            else:
                url = 'http://' + url
            try:
                self.get_href(url)
            except:
                print u'所输入的地址有误或无法访问，请检查___'
                print u'请输入这种格式：http://xxx.xxx.xx 或者 https://xxx.xxx.xx'

    def get_href(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        for a in soup.find_all('a'):
            self.links_check(a['href'])

    def link_check_fina(self):
        for link in links:
            if link != 'http://' and link != 'http://#':
                print link


def main(self):
    queue = Queue.Queue()
    threads = []
    thread_count = 8
    for i in range(thread_count):
        threads.append(spider(queue))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    s=spider()
    s.exec_spider()






