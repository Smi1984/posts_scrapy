from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from posts.items import PostsItem


class PostsSpider(BaseSpider):
    name = "whopost"
    start_urls = [
            "http://osl.ugr.es/"
    ]

    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//*[@id="primary"]/div[@id]')
        print sites
        items = []
        for site in sites:
            item = PostsItem()
            
            item['titulo'] = site.select('h2/a/text()').extract()
            item['autor'] = site.select('div/address/a/text()').extract()
            item['cat'] = site.select('p/span[@class="entry-categories"]/a[@rel="category tag"]/text()').extract() 
            item['tag'] = site.select('p/span[@class="entry-tags"]/a[@rel="tag"]/text()').extract()            
            
            
            #item['contenido'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)
        return items
