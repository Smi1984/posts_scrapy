postsscrapy
============

Test Before Define Spider

1 )
hxs.select('//title/text()')
[<HtmlXPathSelector xpath='//title/text()' data=u'  Oficina de Software Libre de la Univer'>]

2)
hxs.select('//title/text()').extract()
[u'  Oficina de Software Libre de la Universidad de Granada']

3)
vcard = hxs.select('//*[@id="primary"]/div/div/address/a/text()').extract()

for j in vcard:                                                   
    print j.encode('utf-8')
     
admin
Serafín Vélez Barrera
Makova
Renato Luis Ramirez Rivero
Serafín Vélez Barrera

4)
 contenido = hxs.select('//*[@id="primary"]/div/div[2]').extract()

for j in contenido:                                                   
    print j.encode('utf-8')
   ....:     
5)
categorias = hxs.select('//*[@id="primary"]/div/p/span').extract()

6)
tag = hxs.select('//*[@id="primary"]/div/p/span[2]').extract()


