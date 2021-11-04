from flask import render_template

from app.models import Articles
from ..request import get_article, get_sources
from . import main


@main.route('/', methods=['GET'])
def index():
    source = get_sources()


    return render_template('index.html', source=source)


@main.route ('/article/<id>')
def article(id):


    News= get_article(id)
    Articles=get_article(id)

    return render_template('articles.html',News=News, Articles=Articles)
