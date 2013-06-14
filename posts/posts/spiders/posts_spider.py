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
        sites = hxs.select('//ul[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = PostsItem()
            item['titulo'] = site.select('a/text()').extract()
            item['autor'] = site.select('a/@href').extract()
            item['contenido'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)
        return items
