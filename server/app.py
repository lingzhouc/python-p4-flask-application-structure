#!/usr/bin/env python3

from flask import Flask

# __name__ refers to the name of the current module
    # unless it's being run from command line, then it's set to '__main__'
app = Flask(__name__)

# registers index() to application instance
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask run

# option: run dev server from running file
    # python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)