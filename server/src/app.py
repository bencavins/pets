# Two ways of running flask:

# flask --app src/app.py run --port 5555 --debug

from flask import Flask


# initialize our flask app
app = Flask(__name__)


# define your routes
@app.route('/')
def root():
    # returning an html response
    return '<h1>hello world!</h1>', 200  # status code 200 == ok

@app.route('/test')
def test():
    # returning json reponse (very useful for APIs)
    json_data = {
        'key': 'value',
        'test': [1, 2, 3]
    }
    return json_data, 200


# we can parameterize our url strings with flask
@app.route('/hello/<string:name>')
def say_hello(name):

    if name.isdigit():
        return {'your name is a number': int(name)}, 200

    if len(name) <= 1:
        return {'error': 'name too short'}, 400

    return {'hello': name.upper()}, 200


@app.route('/plants/<int:id>')
def plant_by_id(id):
    return {'name': 'sunflower', 'id': id}, 200
