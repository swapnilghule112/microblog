from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Swapnil'}
    posts = [
        {
            'author': {'username': 'vince gilligan'},
            'body': 'Breaking Bad!'
        },
        {
            'author': {'username': 'Walter White'},
            'body': 'How to make meth , 99.9 percent pure?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)