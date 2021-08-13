
import os

class Config:

   	NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
   	NEWS_API_KEY = '0a821ddbec9e472aab79c0bfd2245b41'
	
   	

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}