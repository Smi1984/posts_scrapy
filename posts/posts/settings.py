# Scrapy settings for posts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'posts'

SPIDER_MODULES = ['posts.spiders']
NEWSPIDER_MODULE = 'posts.spiders' 
ITEM_PIPELINES = ['posts.pipelines.JsonWriterPipeline', 
                  'posts.pipelines.XmlExportPipelineWithoutTags',
                  'posts.pipelines.XmlExportPipelineWithTags']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'posts (+http://www.yourdomain.com)'
