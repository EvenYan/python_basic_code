import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        import random
        content = response.xpath('//div[@class="container"]//div[@class="row"]//div[@class="col-md-8"]/div/span/text()').extract()
        filename = 'quotes-%s.txt' % random.randrange(10)
        with open(filename, 'w') as f:
            f.write(str(content))
        self.log('Saved file %s' % filename)
