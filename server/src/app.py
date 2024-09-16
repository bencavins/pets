# Two ways of running flask:

# flask --app src/app.py run --port 5555 --debug

from flask import Flask
from flask_migrate import Migrate
from models import db, Pet


# initialize our flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize sqlalchemy plugin with flask
db.init_app(app)
# initialize Alembic (aka flask migrate)
Migrate(app, db)


# define your routes (flask calls these views)
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


@app.route('/pets/<int:id>')
def plant_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    return pet.to_dict(), 200
