from selenium import webdriver
from mongoengine import connect
from models.NewsUrl import NewsUrl
from configs.FileJsonConfig import FileJsonConfig

from controllers.CommentFactory import CommentFactory

#connect database
connect(db='news_comment_crawler', host='localhost', port=27017)

#block image to optimize loading page capicity
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

# load data from file config json
fileJsonConfig = FileJsonConfig()
listNews = fileJsonConfig.load_config() 

#get domain
def getDomain(url):
    split_url = url.split('/')
    return split_url[2]

# load list url in database
newsUrl = NewsUrl()
urls = newsUrl.getUrl()

for document in urls:
    domain = getDomain(document["name_url"]) #get domain

    # - check domain url with key file json
    for key, value in listNews.items():
        if isinstance(value, dict):
            #print(f"{key}:")
            if(key == domain):

                url = document["name_url"]
                print(url)
                factory = CommentFactory()
                article = factory.createCrawlingComment(domain, driver)
                article.crawlingComment(url, value)
