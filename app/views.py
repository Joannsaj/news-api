from flask import render_template
from app import app

    # message = 'Hello World'
    # return render_template('index.html',massage = message)

@app.route('/')
def index():

    '''
    function that returns the index page and its data
    '''

    title = 'Home - Getting you upto date!'
    return render_template('index.html', title = title)
