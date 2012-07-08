from scrapy.item import Item, Field

class DealItem(Item):
    title = Field()
    subtitle = Field()
    description = Field()
    url = Field()
    
