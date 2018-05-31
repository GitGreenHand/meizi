# -*- coding: utf-8 -*-
import scrapy

from meizi.items import MeiziItem


class MeiziSpiderSpider(scrapy.Spider):
	name = 'meizi_spider'
	# allowed_domains = ['www.baidu.com']
	base_url="http://www.mmjpg.com/mm/1355/"
	start_urls = ['http://www.mmjpg.com/mm/1355/2']

	def parse(self, response):
		image_url = response.xpath('//*[@id="content"]/a/img/@src').extract()
		print('image_url',image_url[0])
		print("*"*40)
		item = MeiziItem()
		item['image_url'] =image_url[0]
		yield item
		for i in range(3,60):
			new_url=self.base_url+str(i)
			yield scrapy.Request(new_url,callback=self.parse)