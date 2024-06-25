# our main flask app
# API == Application Program Interface

# can start flask with
# flask --app src/app.py run --port 5555 --debug

# can also use env vars (don't commit the .env file!!!)
# export FLASK_APP=src/app.py
# export FLASK_RUN_PORT=5555
# export FLASK_DEBUG=1
# flask run
from flask import Flask, make_response, jsonify
from models import db, Pet, Owner
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # how to connect to the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # optional performance thing

db.init_app(app)  # link sqlalchemy with flask
Migrate(app, db)  # set up db migration tool (alembic)


@app.route('/')
def hello():
    json_string = jsonify({'test': 'hello'})  # turn dict into json
    web_resp = make_response(json_string, 200)  # build a web resp
    return web_resp


@app.route('/test')
def test():
    return {'result': 'test'}, 200


# we can add parameters to our routes
@app.route('/upper/<string:word>')
def upper(word):
    new_word = word.upper()
    return {'result': new_word}, 200


@app.route('/dogs')
def dogs():
    # query db for all dog pets
    all_dogs = Pet.query.filter(Pet.type == 'dog').all()
    all_dog_dicts = [d.to_dict() for d in all_dogs]  # turn all dog objs into dicts
    return all_dog_dicts, 200
