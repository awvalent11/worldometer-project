import scrapy


class WorldpopulationSpider(scrapy.Spider):
    name = "worldpopulation"
    allowed_domains = ["worldometers.info"]
    start_urls = ["https://worldometers.info"]

    def parse(self, response):
        pass
