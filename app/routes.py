from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Welcome to my blog</h1>"