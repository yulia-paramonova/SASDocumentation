import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "sasdoc"

    def start_requests(self):
        versions = [
            '9.4_3.4',
            '9.4_3.5',
            'v_024'
        ]
        products = [
            'casstat',
            'casactforecast'
        ]
        urls = [f"https://go.documentation.sas.com/doc/en/pgmsascdc/{version}/{product}/titlepage.htm" for version in versions for product in products]

        
        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 31, 'timeout': 60})

    def parse(self, response):
        # title = response.css("title::text").getall()
        # procs = response.css("div.xis-toc_1 a::text").getall()
        # liens = response.css("div.xis-toc_1 a::attr(href)").getall()
        # self.log(response.url)
        # self.log(title)
        # self.log(procs)
        # self.log(liens)
        for el in response.css('div.xis-toc_1'):
            yield {
                'title': response.css("title::text").get(),
                'name': el.css('a::text').get(),
                'link': el.css('a::attr(href)').get()
            }
        # self.log(body)
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')