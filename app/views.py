from flask import render_template
from app import app
from .request import get_sources

    # message = 'Hello World'
    # return render_template('index.html',massage = message)

@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''
    general_sources = get_sources('general')
    print(general_sources)
    title = 'Home - Getting you upto date!'
    return render_template('index.html', title = title,general = general_sources)
# general, sports,technology,science,entertainment