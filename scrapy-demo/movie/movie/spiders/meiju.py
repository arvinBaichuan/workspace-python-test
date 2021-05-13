# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import scrapy
from items import MovieItem

class MeijuSpider(scrapy.Spider):
    print('测试1-》')
    name = 'meiju'
    allowed_domains = ['www.meijutt.tv']
    start_urls = ['http://www.meijutt.tv/']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        print('测试2-》')
        print(movies)
        for each_movie in movies:
            print('测试3-》'+each_movie)
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
