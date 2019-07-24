# -*- coding: utf-8 -*-
import requests
import BeautifulSoup
import sys
import threading
import json
import Queue

url = ''
headers = {}
links = set()

class spider(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            num = self.queue.get()
            self.exec_spider(num)

    def exec_spider(num):
        r = requests.post(url=url, headers=headers, data={'':''})
        data = json.loads(r.text)


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
    main()




#判断空链接与不符合条件的结果
def links_check(link):
    if link != '#' and link!= '' and '(' not in link:
        link_parse(link)
#对获得的链接进行补全
def link_parse(r_link):
    if '://' in r_link:
        links.add(r_link)
    if '://' not in r_link:
        r_link ='http://10.1.1.155' + r_link
        links.add(r_link)
    return links

def url_parse(url):
    if 'http' in url:
        try:
            get_href(url)
        except:
            print u'所输入的地址有误或无法访问，请检查----'
            print u'请输入这种格式：http://xxx.xxx.xx 或者 https://xxx.xxx.xx'
        else:
            url = 'http://' +url
        try:
            get_href(url)
        except:
            print u'所输入的地址有误或无法访问，请检查___'
            print u'请输入这种格式：http://xxx.xxx.xx 或者 https://xxx.xxx.xx'

def get_href(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    for a in soup.find_all('a'):
        links_check(a['href'])

def link_check_fina():
    for link in links:
        if link !='http://' and link != 'http://#':
            print link
