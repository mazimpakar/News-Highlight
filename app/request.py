from app import app
import urllib.request,json
from .models import news
# Source, News

News = news.News
Source = news.Source


# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]
news_base_url = app.config["NEWS_NEWS_API_BASE_URL"]
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category, api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

        # print(source_results)
    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        news_id= source_item.get('id')
        name= source_item.get('name')
        url  = source_item.get('url')
        description =source_item.get('description')
        # language = source_item.get('language')

        
        source_object = Source(news_id,name,url ,description)
        source_results.append(source_object)

    return source_results 



def get_news(name):
    '''Function thet gets the json response to our url request'''
    get_news_url = news_base_url.format(name,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news(news_results_list)
            
    
    return news_results

def process_news(news_list):
    '''
    Function that processes the news result and transforms them to a list of objects
    Args:
        news_list: a list of dictionaries that contain news
    Returns:
        news_results: a list of news objects
    '''
    # print(news_list)
    news_results = []
    for news_item in news_list:
        # name = news_item.get('name')
        author= news_item.get('author')
        title = news_item.get('title')
        urlToImage = news_item.get('urlToImage')
        description = news_item.get('description')
        url=news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        if author:
            news_object = News(author,title,urlToImage,description,url,publishedAt,content)
            news_results.append(news_object)
    return news_results




















    








