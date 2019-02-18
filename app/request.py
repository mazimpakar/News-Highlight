from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

        print(news_results)
    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name= news_item.get('name')
        author= news_item.get('author')
        title = news_item.get('title')
        urlImage  = news_item.get('urlImage')
        description =news_item.get('description')
        publishedAt = news_item.get('publishedAt')

        
        news_object = News(name,author,title,urlImage ,description,publishedAt)
        news_results.append(news_object)

    return news_results 



