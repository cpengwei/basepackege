#encoding:utf-8
import json

from pyquery import PyQuery
import requests

class Movie(object):

    def __init__(self):
        self.url = r'https://maoyan.com/board/4?offset='
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

    def get_movies(self,html):
        doc=PyQuery(html)
        for item in doc.items('.board-item-content'):
            return {
                'name':item.find('.name').text(),
                'stars':item.find('.star').text().split('：')[1],
                'time':item.find('.releasetime').text().split('：')[1],
                'score':item.find('.score').text()
            }

    def parse_url(self,page_num):
        url=self.url + str(page_num)
        try:
            r=requests.get(url,headers=self.header)
            return r.text
        except Exception as e:
            print('url parses faild',e)
            return None

if __name__ == '__main__':

    crawl =Movie()
    for n in range(11):
        html = crawl.parse_url(n)
        movies = crawl.get_movies(html)
        #for movie in movies:
        print(movies)

