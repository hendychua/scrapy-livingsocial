from scrapy.exceptions import DropItem

class AlcoholPipeline(object):
    
    def process_item(self, item, spider):
        if "wine" in unicode(item['subtitle'][0]).lower():
            raise DropItem("Alcohol is bad")
        else:
            if not item["description"]:
                return item
            else:
                if "wine" in unicode(item["description"][0]).lower():
                    raise DropItem("Alcohol is bad")
                else:
                    return item
