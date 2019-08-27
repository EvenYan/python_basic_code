import scrapy

class BlogSpider(scrapy.Spider):
    name = "blog"

    def start_requests(self):
        urls = [
            'http://www.evenyan.com/post/6'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        file_name = 'post-%s.html' % page
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('文件%s保存成功' % file_name)
