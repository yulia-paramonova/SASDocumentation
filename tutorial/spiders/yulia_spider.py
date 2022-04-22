import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
	name = "procedures"

	def start_requests(self):
		versions = [
			'9.4_3.4',
			'9.4_3.5',
			'v_006',
			'v_013',
			'v_019',
			'v_024',
			'v_025'
		]
		products = [
			'casecon',
			'casml',
			'casforecast',
			'casstat',
			'casvta'
		]
		urls = [f"https://go.documentation.sas.com/doc/en/pgmsascdc/{version}/{product}/titlepage.htm"	for version in versions	for product in products]

		for	url	in urls:
			yield SplashRequest(url, self.parse, args={'wait': 31, 'timeout': 60})

	def parse(self, response):
		for el in response.css('div.xis-toc_1'):
				yield {
						'product': response.css('a.breadcrumb-link::text').get(),
						'version': response.css('div.VersionPicker_versionPicker__hoPBe a::text').get(),
						'procedure': el.css('a::text').get(),
						'link': el.css('a::attr(href)').get()
						}