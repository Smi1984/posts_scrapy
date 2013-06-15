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
        
        items = []
        
        
        for site in sites:
            i=0
            aux=[]
            item = PostsItem()
           
            it = site.select('h2/a/text()').extract()
            if len(it) == 1:
				aux.append(it[0].encode('utf-8'))		
            elif len(it) > 1:
				i = 0
				for aut in it:
					aux.append(aut[i].encode('utf-8'))
					i = i + 1
            item['titulo'] = aux              
            ########################################################
            aux = []
            it = site.select('div/address/a/text()').extract()	
            				 
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))
            elif len(it) > 1:
				i = 0
				for aut in it:
					aux.append(aut[i].encode('utf-8'))
					i = i + 1
            item['autor'] = aux   
				  		
			########################################################		                      
            
            aux = []
            it = site.select('p/span[@class="entry-categories"]/a[@rel="category tag"]/text()').extract()
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))
            elif len(it) > 1:
				i = 0
				for aut in it:
					aux.append(aut.encode('utf-8'))
					i = i + 1
					
            item['cat'] = aux  
            ########################################################					 
            
            aux =[]
            it = site.select('p/span[@class="entry-tags"]/a[@rel="tag"]/text()').extract()
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))	 
            elif len(it) > 1:
				i = 0
				for aut in it:
					aux.append(aut.encode('utf-8'))
					i = i + 1
            item['tag'] = aux  
	
            ########################################################	 
           
         
            #item['tag'] = site.select('p/span[@class="entry-tags"]/a[@rel="tag"]/text()').extract()
            
            
            #item['contenido'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)
        return items
