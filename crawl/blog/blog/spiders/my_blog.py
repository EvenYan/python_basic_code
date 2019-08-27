# -*- coding: utf-8 -*-
import scrapy


class MyBlogSpider(scrapy.Spider):
    name = 'my_blog'
    allowed_domains = ['evenyan.com']
    start_urls = ['http://evenyan.com/']

    def parse(self, response):
        name = response.xpath('//article/h1/a/text()').extract()
        print(name)
