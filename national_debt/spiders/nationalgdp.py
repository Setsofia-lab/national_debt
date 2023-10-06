import scrapy


class NationalgdpSpider(scrapy.Spider):
    name = 'nationalgdp'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/country-rankings/countries-by-national-debt/']

    def parse(self, response):
        nationgdp = response.xpath("//table/tr/td[2]")
        for rank in nationgdp:
            nation = rank.xpath(".//td[2]/text()").get()
            gdp = rank.xpath(".//td[3]/text()").get()

            yield{
                'nation': nation,
                'gdp': gdp
            }

