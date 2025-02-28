import scrapy

from bookscraper.items import BookscraperItem

class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["https://books.toscrape.com/"]
    
    
    def parse(self, response):
        
        for i in response.css('article.product_pod'):
            item = BookscraperItem()
            item["title"] = i.css('h3 a::text').get()
            item["price"] = i.css('div.product_price p::text').get()
            
            yield item  
            
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
        