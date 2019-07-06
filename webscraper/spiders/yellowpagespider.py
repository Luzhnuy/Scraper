import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class YellowPagesSpider(CrawlSpider):
    name = "yp"
    start_urls = [
        "https://www.yellowpages.com/austin-tx/plumbers?",
        # "https://www.yellowpages.com/austin-tx/plumbers?page=2"
    ]
    rules = (
        Rule(LinkExtractor(allow=('page=\d+',)), callback='parse_page'),
    )

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        # print(response.css('div.search-results.organic'))
        print("1---------------------------------------------------1")
        for item in response.css('div.result'):
            # print(item)
            print('-------------------------------------------------')
            links = item.css('div.links')
            links = re.sub(r'\<[^>]*\>', '', str(links.extract()))
            print(links.encode('utf-8'))
            if "Directions" in links:
                title = item.css('div.info>h2.n')
                title = re.sub(r'\<[^>]*\>', '', str(title.extract()))
                print(title.encode('utf-8'))
