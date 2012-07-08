from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from livingsocial_crawler.items import DealItem

class LivingSocialSpider(BaseSpider):
    
    base_uri = "http://www.livingsocial.com/"
    
    name = "livingSocialSpider"
    allowed_domains = ["livingsocial.com"]
    start_urls = [base_uri]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        deals = []
        
        ## Get all the hrefs to the deals so we can go to the page and get details
        all_deals_link = hxs.select('//div[@class="deal-image"]/a/@href').extract()
        
        ## Go to every deal's page and get the data we want
        for link in all_deals_link:
            deal_item = Request(url=self.base_uri+link, callback=self.parse_deals)
            deals.append(deal_item)
            
        return deals
        
    def parse_deals(self, response):
        hxs = HtmlXPathSelector(response)
        
        deal_item = DealItem()
        deal_item['title'] = hxs.select("//div[@class='deal-title']/h1/text()").extract()
        deal_item['subtitle'] = hxs.select("//div[@class='deal-title']/p/text()").extract()
        deal_item['description'] = hxs.select("//div[@id='view-details-full']/p").extract()
        deal_item['url'] = response.url
        
        return deal_item
