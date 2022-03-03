import scrapy

# camelCase class names


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
