import scrapy
from cogikSpider.items import CogikSpiderItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://book.douban.com/tag/']
    url = 'https://book.douban.com'

    def parse(self, response):
        tags = response.xpath(
            '//table[@class="tagCol"]/tbody/tr/td/a/@href').extract()
        for tag in tags:
            print(self.url + tag)
            yield scrapy.Request(self.url + tag, callback=self.parse_books)

    def parse_books(self, response):
        books = response.xpath('//li[@class="subject-item"]')
        books_tag_tmp = response.xpath(
            '//title/text()').extract_first().strip()
        books_tag = books_tag_tmp[books_tag_tmp.rfind(':') + 1:].strip()
        for book in books:
            bookItem = CogikSpiderItem()
            bookItem['label'] = book.xpath(
                '//div[@class="info"]/h2/a/text()').extract_first().strip()
            book_url = book.xpath(
                '///div[@class="info"]/h2/a/@href').extract_first().strip()
            tmp_url = book_url[:-1]
            book_id = tmp_url[tmp_url.rfind('/') + 1:]
            bookItem['item_id'] = book_id
            attr = {'url': book_url, 'book_tag': books_tag}
            bookItem['attr'] = attr
            print(bookItem)
            yield bookItem

        next_link = response.xpath(
            '//span[@class="next"]/a/@href').extract_first()
        if next_link:
            yield scrapy.Request(self.url + next_link,
                                 callback=self.parse_books)
