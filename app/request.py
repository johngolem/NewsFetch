import urllib.request
import json
from .models import NewsSource, Articles


# Fetch API key
api_key = 'c445d1b3d30e47cbbb9c199771e8d3a9'

# Fetch News Base Url
source_base_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
article_base_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


def configure_request(app):
    global api_key, source_base_url, article_base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['SOURCE_BASE_URL']
    article_base_url = app.config['ARTICLE_BASE_URL']


def get_sources():
    url_for_sources = source_base_url.format(api_key)
    print(url_for_sources)
    with urllib.request.urlopen(url_for_sources) as data:
        sources_data = data.read()
        sources_response = json.loads(sources_data)
        
        sources_results = None
        
        if sources_response['sources']:
            sources_results_list = sources_response['sources']
            sources_results = process_source_results(sources_results_list)
    return sources_results

def process_source_results(sources_list):
    sources_results = []
    for news_source in sources_list:
        source_name = news_source.get('name')
        source_id = news_source.get('id')
        source_url = news_source.get('url')
        source_category = news_source.get('category')
        
        source_object = NewsSource(source_name,source_id,source_url,source_category)
        sources_results.append(source_object)
        
    return sources_results

def get_article(category):
    get_article_url=article_base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        articles_data=url.read()
        article_response =json.loads(articles_data)

        articles_results=[]

        if article_response['articles']:
            articles_results_list=article_response['articles']
            articles_results = process_articles(articles_results_list)
            print(articles_results)
    return articles_results

def process_articles(articles_results_list):
        '''
        Function that processes the news articles result and transform them to a list of objects
        Args:
            article_list: a list of dictionaries that contain news articles details
        Returns:
            articles_result: a list of news articles objects
        '''
        articles_results = []
        
        for article_item in articles_results_list:
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            content = article_item.get('content')
            id = article_item.get('id')
            
            if urlToImage:
                articles_object = Articles(author,title,description,url,urlToImage,publishedAt,content,id)
                articles_results.append(articles_object)
        return articles_results
 
           


    