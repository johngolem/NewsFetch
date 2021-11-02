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

def get_articles():
    

    