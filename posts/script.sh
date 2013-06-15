rm items.jl
rm *.xml
scrapy crawl whopost -t json
scrapy crawl whopost -t xml
geany items.jl &

