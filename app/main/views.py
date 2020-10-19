from flask import render_template
from . import main
from .request import get_sources,get_articles
from ..models import 
    # message = 'Hello World'
    # return render_template('index.html',massage = message)

@main.route('/')
def index():

    '''
    function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    science_sources = get_sources('science')
    entertainment_sources = get_sources('entertainment')

    title = 'Home - Getting you upto date!'
    return render_template('index.html', title = title,general = general_sources,sports= sports_sources, technology =technology_sources, science=science_sources, entertainment=entertainment_sources)
# general, sports,technology,science,entertainment

@main.route('/articles/<source_id>')
def article(source_id):
    title = f'{source_id}'
    source_articles = get_articles(source_id)
    return render_template('article.html', title=title, articles = source_articles)