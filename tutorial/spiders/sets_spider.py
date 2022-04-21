import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "sets"

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
        urls = [f"https://go.documentation.sas.com/doc/en/pgmsascdc/{version}/allprodsactions/actionSetsByProduct.htm" for version in versions]

        
        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 31, 'timeout': 60})

    def product_parse(self, response):
        for row in response.css('tr'):
            columns = row.css('td')
            try:
                if len(columns)<3:
                    yield {
                        'product': response.css('h1.xisCas-title::text').get(),
                        'version': response.css('div.VersionPicker_versionPicker__hoPBe a::text').get(),
                        'action_set_name': columns[0].css('a::text').get(),
                        'set_link': columns[0].css('a::attr(href)').get(),
                        'description': columns[1].css('td::text').get()
                    }
                else:
                    yield {
                        'product': response.css('h1.xisCas-title::text').get(),
                        'version': response.css('div.VersionPicker_versionPicker__hoPBe a::text').get(),
                        'action_set_name': columns[0].css('a::text').get(),
                        'set_link': columns[0].css('a::attr(href)').get(),
                        'description': columns[2].css('td::text').get()
                    }
            except IndexError:
                self.log("IndexError")
                self.log(row.get())

    def parse(self, response):
        for el in response.css('div.xisDoc-toc_1'):
            product_page = el.css('a::attr(href)').get()
            if product_page is not None:
                product_page = response.urljoin(product_page)
                yield SplashRequest(product_page, self.product_parse, args={'wait': 40, 'timeout': 60})
            