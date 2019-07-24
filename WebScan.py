import sys
import requests
import Queue
import threading

url = 'http://192.168.74.141/DVWA-1.9/'
headers = {}

class DirScan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        self.scan()

    def scan(self):
        while not self.queue.empty():
            url = self.queue.get()
            try:
                r = requests.get(url = url,headers = headers,timeout=5)
                if r.status_code == 200:
                    sys.stdout.write('[+]%s\t\t\n' % url)
            except:
                pass

def main():

    url_queue = Queue.Queue()
    threads = []
    thread_num = 8
    f = open("dic.txt",'r')
    for i in f:
        url_queue.put(url + i.strip('\n'))
    for i in range(thread_num):
        threads.append(DirScan(url_queue))
    for i in threads:
        i.start()
    for i in threads:
        i.join()

if __name__ == '__main__':
    main()
