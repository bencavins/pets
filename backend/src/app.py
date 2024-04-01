"""
One way of running the app:
flask --app src/app.py --debug run --port 5555


We can also use environment variables:
export FLASK_APP=src/app.py  # this is a path, make sure it is correct!
export FLASK_RUN_PORT=5555
export FLASK_DEBUG=1

Then we just need to do:
flask run
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def root():
    return '<h1>HELLO</h1>'

@app.route('/helloworld')
def hello_world():
    return {'message': 'goodbye world!'}

@app.route('/user/<int:id>')
def user_by_id(id):
    return {'your user id is': id}