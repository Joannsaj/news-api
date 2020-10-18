class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_ARTICLE_API='https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_SOURCE_API='https://newsapi.org/v2/sources?apiKey={}'



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True