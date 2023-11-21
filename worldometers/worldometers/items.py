import scrapy

class WorldometersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    population = scrapy.Field()
    yearly_perc_change = scrapy.Field()
    yearly_change = scrapy.Field()
    migrants = scrapy.Field()
    median_age = scrapy.Field()
    fert_rate = scrapy.Field()
    density = scrapy.Field()
    urban_pop_perc = scrapy.Field()
    urban_pop = scrapy.Field()
    perc_pop_worldwide = scrapy.Field()
    world_pop = scrapy.Field()
    global_rank = scrapy.Field()