import urllib.request,json
from .models import Source
from .models import Article

api_key = None
source_url =None
article_url = None
# Source = source.Source
# Article = article.Article
def configure_request(app):
    global api_key,source_url,article_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config["NEWS_SOURCE_API"]
    article_url = app.config["NEWS_ARTICLE_API"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)


    return source_results

def process_results(source_list):
    
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')


        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

    return source_results

def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(source_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_response(article_results_list)


    return article_results

def process_response(article_list):
    
    article_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Article(source,author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results    