import urllib.request,json
from .models import news_Article, news_Source

# Getting api key
api_key = None

# Getting the movie base url
base_url = None
articles_url=None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    # articles_url=app.config['NEWS_API_ARTICLES_URL']



def get_news_sources():
    '''
    Function that gets the json responce to our url request
    '''
    get_news_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_results_list = get_news_source_response['sources']
            news_source_results = process_results(news_source_results_list)


    return news_source_results
def get_news_source(source):
    '''
    Function that gets the json responce to our url request
    '''
    base_url='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    get_news_source_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)
        print(get_news_source_response)
        news_source_results = None

        if get_news_source_response['articles']:
            news_source_results_list = get_news_source_response['articles']
            news_source_results = process_articles_results(news_source_results_list)


    return news_source_results
def process_articles_results(news_articles_results):
    '''
    Function  that processes the news source result and transform them to a list of Objects
    Args:
        news_sources_list: A list of dictionaries that contain news details
    Returns :
        news_source_results: A list of news sources objects
    '''
    news_results = []
    
    for news_article_item in news_articles_results:
        author = news_article_item.get('author')
        title = news_article_item.get('title')
        description = news_article_item.get('description')
        url = news_article_item.get('url')
        imageurl = news_article_item.get('urlToImage')

        news_source_object = news_Article(author,title,description,url,imageurl)
        news_results.append(news_source_object)
        print(news_results)
          
    return news_results

def process_results(news_source_results):
    '''
    Function  that processes the news source result and transform them to a list of Objects
    Args:
        news_sources_list: A list of dictionaries that contain news details
    Returns :
        news_source_results: A list of news sources objects
    '''
    news_sources_results = []
    
    for news_source_item in news_sources_results:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        language = news_source_item.get('language')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        

        news_source_object = news_Source(id,name,description,url,language,)
        news_sources_results.append(news_source_object)

    return news_source_results