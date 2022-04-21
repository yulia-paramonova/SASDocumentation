import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "actions"

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
        urls = [f"https://go.documentation.sas.com/doc/en/pgmsascdc/{version}/allprodsactions/actionsByName.htm" for version in versions]

        
        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 31, 'timeout': 60})


    def parse(self, response):
        for row in response.css('tr'):
            columns = row.css('td')
            try:
                if columns.css('td')[0].css('a::text').get() is not None:
                    yield {
                        'version': response.css('div.VersionPicker_versionPicker__hoPBe a::text').get(),
                        'action_name': columns.css('td')[0].css('a::text').get(),
                        'link': columns.css('td')[0].css('a::attr(href)').get(),
                        'description': columns.css('td')[1].css('td::text').get(),
                        'action_set_name': columns.css('td')[2].css('td::text').get()
                    }
                else:
                    yield {
                        'version': response.css('div.VersionPicker_versionPicker__hoPBe a::text').get(),
                        'action_name': columns.css('td')[0].css('span.xisDoc-glossTerm::text').get(),
                        'link': "unknown",
                        'description': columns.css('td')[1].css('td::text').get(),
                        'action_set_name': columns.css('td')[2].css('td::text').get()
                    }
            except IndexError:
                pass
            