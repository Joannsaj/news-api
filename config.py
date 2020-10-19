import os

class Config:

    NEWS_ARTICLE_API='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_SOURCE_API='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

