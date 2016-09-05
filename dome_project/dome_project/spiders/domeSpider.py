#coding:utf-8
import re

import scrapy

from dome_project.items import DomeProjectItem
from dome_project.settings import setting_day,setting_mon


class domeSpider(scrapy.Spider):
    name = 'dome'
    start_urls = ['http://wallstreetcn.com/news']

    def parse(self,response):

        for selector in  response.xpath('//ul[@class="news-list with-img"]/li[@class="news"]'):
            item = DomeProjectItem()

            title = selector.xpath('div[@class="content"]/a/text()').extract()[0].strip()
            item['title'] = title
            time = selector.xpath('div[@class="content"]/div/span[@class="meta time visible-lg-inline-block"]/text()').extract()[0]
            item['time'] = time
            yield item
        flat =  response.xpath('//span[@class="meta time visible-lg-inline-block"]/text()').extract()[0]
        flat_list = re.findall(r'2016年(.*?)月(.*?)日',flat.encode('utf-8'))
        day = int(flat_list[0][1])
        mon = int(flat_list[0][0])

        if mon >= setting_mon and day >= setting_day:
            print flat_list
            next_url = response.xpath('//i[@class="fa fa-angle-right"]/../@href').extract()[0]
            print next_url
            yield scrapy.Request(url = next_url,callback=self.parse)