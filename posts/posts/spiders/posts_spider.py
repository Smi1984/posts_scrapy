from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from posts.items import PostsItem
from bs4 import BeautifulSoup
import re

class PostsSpider(BaseSpider):
    name = "whopost"
    start_urls = [
            "http://osl.ugr.es/"
    ]

    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select("//div[@class='entry hentry']")        
        items = []
        
        
        for site in sites:

            aux=[]
            item = PostsItem()
           
            it = site.select('h2/a/text()').extract()
            if len(it) == 1:
				aux.append(it[0].encode('utf-8'))		
            elif len(it) > 1:
				for aut in it:
					aux.append(aut[i].encode('utf-8'))
            item['titulo'] = aux              
            ########################################################
            aux = []
            it = site.select('div/address/a/text()').extract()	
            				 
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))
            elif len(it) > 1:
				for aut in it:
					aux.append(aut[i].encode('utf-8'))
            item['autor'] = aux   
				  		
			########################################################		                      
            
            aux = []
            it = site.select('p/span[@class="entry-categories"]/a[@rel="category tag"]/text()').extract()
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))
            elif len(it) > 1:
				for aut in it:
					aux.append(aut.encode('utf-8'))
					
            item['cat'] = aux  
            ########################################################					 
            
            aux =[]
            it = site.select('p/span[@class="entry-tags"]/a[@rel="tag"]/text()').extract()
            if len(it) == 1: 
				aux.append(it[0].encode('utf-8'))	 
            elif len(it) > 1:
				for aut in it:
					aux.append(aut.encode('utf-8'))

            item['tag'] = aux  
	
            ########################################################	 
 
            aux =[]
            it = hxs.select("//div[@class='entry-content']").extract()
            if len(it) == 1: 
				soup = BeautifulSoup(it[0],from_encoding="utf-8")
				aux.append(soup.get_text().encode('utf-8'))	 
            elif len(it) > 1:
				for aut in it:
				    soup = BeautifulSoup(aut,from_encoding="utf-8")
				    aux.append(soup.get_text().encode('utf-8'))	 					
            item['contenido'] = aux   

            
            items.append(item)
        return items
