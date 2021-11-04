from flask import render_template,request,redirect,url_for
from app.models import Articles
from ..request import get_article, get_sources
from . import main


# @main.route('/', methods=['GET'])
@main.route('/',methods=[ 'POST','GET'])
def index():


    raw_data = ""
    articles= get_article('creative')
    if request.method == 'POST':
        query_str = request.form.get("query")
        articles = get_article(query_str)
        
    # if not (raw_data):
    # articles = get_articles('') 

    data = {
        "title":"The News Man",
        "heading": "NewsMan", 
    }
    source = get_sources()


    # return render_template('index.html', source=source)


# @main.route ('/article/<category>')
# def article(category):


#     News= get_article(category)
#     Articles=get_article(category)

    return render_template('index.html', context=data,source=source, article=articles)
