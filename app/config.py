class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=f64a31e5dca5460ab7e3f34713eb9670'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=f64a31e5dca5460ab7e3f34713eb9670
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True