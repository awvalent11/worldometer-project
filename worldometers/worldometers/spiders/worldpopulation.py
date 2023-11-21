import logging
import scrapy
# from worldometers.items import WorldometersItem
from datetime import datetime

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

class WorldpopulationSpider(scrapy.Spider):
    '''CREATED SPIDER NAMED WORLDPOPULATIONSPIDER TO SCRAPE DATA FROM WORLDOMETERS'''

    # SPIDER NAME
    name = 'worldpopulation'
    allowed_domains = ['worldometers.info']
    # SPIDER START SCRAPING FROM 'start_urls'
    start_urls = ['https://www.worldometers.info/world-population/pakistan-population/']

    def parse(self, response):

        item= WorldometersItem()
        logging.info('start scraping data from worldometer')
        for num_of_years in range(1, 18):
            # YEAR. TYPE= STRING. DB= TIME(YEAR)
            item['year']= datetime.strptime(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[1]//text()').get(), '%Y')

            # POPULATION. TYPE= STRING, WITH COMMAS. DB= INTEGAR
            population= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[2]/strong//text()').get())
            item['population']= self.remove_commas(population)

            # YEARLY % CHANGE. TYPE= STRING, WITH PERCENT SIGN. DB= FLOAT + PERCENT
            yearly_perc_change= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[3]//text()').get())
            item['yearly_perc_change']= self.perc_to_float(yearly_perc_change)

            # YEARLY CHANGE. TYPE= STRING, WITH COMMAS. DB= INTEGAR
            yearly_change= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[4]//text()').get())
            item['yearly_change']= self.remove_commas(yearly_change)

            # MIGRANTS (NET). TYPE= STRING, WITH COMMAS AND NEGATIVE SIGN. DB= INTEGAR
            migrants= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[5]//text()').get())
            item['migrants']= self.remove_commas(migrants)

            # MEDIAN AGE. TYPE= STRING. DB= FLOAT
            item['median_age']= float(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[6]//text()').get())

            # FERTILITY RATE. TYPE= STRING. DB= FLOAT
            item['fert_rate']= float(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[7]//text()').get())

            # DENSITY (P/Km2). TYPE= STRING. DB= INTEGAR
            item['density']= int(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[8]//text()').get())

            # UBRAN POP %. TYPE= STRING, WITH PECENT SIGN. DB= FLOAT + PERCENT
            urban_pop_perc= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[9]//text()').get())
            item['urban_pop_perc']= self.perc_to_float(urban_pop_perc)

            # URBAN POPULATION. TYPE= STRING, WITH COMMAS. DB= INTEGAR
            urban_pop= str(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[10]//text()').get())
            item['urban_pop'] = self.remove_commas(urban_pop)

            # COUNTRY'S SHARE OF WORLD POPULATION. TYPE= STING, WITH PERCENT SIGN. DB= FLOAT + PERCENT
            perc_pop_worldwide= response.xpath(f'//table/tbody/tr[{num_of_years}]/td[11]//text()').get()
            item['perc_pop_worldwide']= self.perc_to_float(perc_pop_worldwide)

            # WORLD POPULATION. TYPE= STRING, WITH COMMAS. DB= INTEGAR
            world_pop= response.xpath(f'//table/tbody/tr[{num_of_years}]/td[12]//text()').get()
            item['world_pop']= self.remove_commas(world_pop)

            # GLOBAL RANK. TYPE= STRING. DB= INTEGAR
            item['global_rank']= int(response.xpath(f'//table/tbody/tr[{num_of_years}]/td[13]//text()').get())

            yield item

    # FUNCTION TO REMOVE COMMAS FROM THE STRING AND CHANGE THE STRING INTO INTEGAR DATA TYPE
    def remove_commas(self, strng):
        strng= int(strng.replace(",", ""))
        return strng

    # FUNCTION TO REMOVE PERCENT SIGN FROM STRING AND CONVERT THE STRING TO FLOAT DATA TYPE
    def perc_to_float(self, strng):
        strng= float(strng.replace('%', '').strip())
        return strng