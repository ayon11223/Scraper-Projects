import scrapy
from countryinfo.items import CountryinfoItem
class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        countryinfo = response.css('div.col-md-4')   
        for i in countryinfo:
            item = CountryinfoItem()
            item["name"] = i.xpath("normalize-space(.//h3[@class='country-name'])").get()
            item["capital"] = i.css('span.country-capital::text').get()
            item["population"] = i.css('span.country-population::text').get()
            item["area"] = i.css('span.country-area::text').get()
                
            yield item
