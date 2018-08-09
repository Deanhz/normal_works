import scrapy
from cogikSpider.items import CogikSpiderItem


class MovieSpider(scrapy.Spider):
    name = "qq_movie"
    allowed_domains = ["v.qq.com"]
    start_urls = [
        "http://v.qq.com/x/list/movie",

    ]
    url = "http://v.qq.com/x/list/movie"

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = CogikSpiderItem()
            item['label'] = sel.xpath('div/strong/a/text()').extract()
            if item['label']:
                item['label'] = item['label'][0]
                movie_url = sel.xpath('div/strong/a/@href').extract()[0]
                attr = {'url': movie_url}
                item_id = 'movie-tv-' + \
                    str(movie_url).split('/')[-1].split('.')[0]
                item['item_id'] = item_id
                item['attr'] = attr
                yield item

        nextlink = response.xpath(
            '//div/a[@class="page_next"]/@href').extract()
        if nextlink:
            link = nextlink[0]
            yield scrapy.Request(self.url + link, callback=self.parse)
