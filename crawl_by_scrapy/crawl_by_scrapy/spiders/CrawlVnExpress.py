# import scrapy
#
#
# class Crawl24hSpider(scrapy.Spider):
#     name = "CrawlVnExpress"
#     allowed_domains = ["vnexpress.net"]
#     start_urls = ["https://vnexpress.net/"]
#
#
#     def parse(self, response):
#         #Lấy các tiêu đề bằng css selector
#         #Sử dụng CSS selector để tìm các thẻ <a> nằm trong các thẻ <h3> có lớp title-news
#         #Sau đó getall để lấy tất các kết quả có css như vậy
#         titles = response.css('h3.title-news a::text').getall()
#
#         index = 0
#         for title in titles:
#             #Để in ra và có thể lưu dữ liệu vào file Json hoặc Csv
#             yield {'STT': index, 'Title': title}
#             index += 1
#
#
#

import scrapy
class VnexpressSpider(scrapy.Spider):
    name = 'CrawlVnExpress'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/']

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title': article.css('h3.title-news a::text').get(),
                'description': article.css('p.description a::text').get(),
                'image_url': article.css('img::attr(src)').get(),
                'link': article.css('h3.title-news a::attr(href)').get(),
            }

