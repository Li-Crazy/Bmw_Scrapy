# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.bmw.bmw.items import BmwItem

class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/202.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxs:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text("
                                   ")").get()
            # print(category)
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     # url = "https:" + url
            #     url = response.urljoin(url)
            #     print(url)

            urls = list(map(lambda url:response.urljoin(url),urls))
            print(urls)
            # item = BmwItem(category=category,urls=urls)
            item = BmwItem(category=category,image_urls=urls)
            yield item

