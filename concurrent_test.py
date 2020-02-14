#encoding:utf-8

from pyquery import PyQuery
import requests
from datetime import datetime
import threading
import queue

def get_movies(html):
    doc=PyQuery(html)
    for item in doc.items('.board-item-content'):
        return {
            'name':item.find('.name').text(),
            'stars':item.find('.star').text().split('：')[1],
            'time':item.find('.releasetime').text().split('：')[1],
            'score':item.find('.score').text()
        }

def parse_url(page_num):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    url=r'https://maoyan.com/board/4?offset={}'.format(page_num)
    movieslist = []
    try:
        r=requests.get(url,headers=headers)
        movies = get_movies(r.text)
        # for movie in movies:
        #     movieslist.append(movie)
        print(movies)
    except Exception as e:
        print('url parses faild',e)
        return None

class MyThread(threading.Thread):
    def __init__(self,fun):
        threading.Thread.__init__(self)
        self.fun = fun
    def run(self):
        self.fun()

def worker():
    while not q.empty():
        item = q.get()  # 获得任务
        parse_url(item)

def main(q,num):#num为线程数
    threads = []
    for task in range(0, 91, 10):
        q.put(task)
    for n in range(num):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for item in threads:
        item.join()

if __name__ == '__main__':
    start_time = datetime.now()
    for n in range(0,91,10):
        parse_url(n)
    end_time = datetime.now()
    print('普通方式花费时间：{}s'.format(end_time-start_time))
    q = queue.Queue()
    start_time1 = datetime.now()
    main(q,4)
    end_time1 = datetime.now()
    print('3个线程花费时间：{}s'.format(end_time1-start_time1))
