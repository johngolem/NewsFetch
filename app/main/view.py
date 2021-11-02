from flask import render_template
from ..request import get_sources
from . import main


@main.route('/', methods=['GET'])
def index():
    source = get_sources()
    print(source)

    return render_template('index.html', source=source)
