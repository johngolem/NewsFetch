import urllib.request
from urllib.parse import quote
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

def get_article(source):
    
    get_article_url = article_base_url.format(source,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)
        
        articles_results = None
        
        if article_response['articles']:
            articles_results_list = article_response['articles']
            articles_results = process_article(articles_results_list)
    return articles_results
def process_article(articles_list):

        articles_results = []
        for articles in articles_list:
            author = articles.get('author')
            title = articles.get('title')
            description = articles.get('description')
            url = articles.get('url')
            urlToImage = articles.get('urlToImage')
            publish = articles.get('publishedAt')
            content = articles.get('content')
           
            article_object = Articles(author,title,description,url,urlToImage,publish,content)
            articles_results.append(article_object)
                
        return articles_results
                
    

    