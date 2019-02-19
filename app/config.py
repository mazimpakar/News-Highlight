class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY ='f64a31e5dca5460ab7e3f34713eb9670' 
    pass


class DevConfig(Config):
    '''https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=f64a31e5dca5460ab7e3f34713eb9670
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True