# Two ways of running flask:

# flask --app src/app.py run --port 5555 --debug

# API == Application Programming Interface
# HTTP == common protocol
# REST == Representational State Transfer
#   - useful design pattern for APIs

from flask import Flask, request
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


@app.route('/pets', methods=['GET', 'POST'])
def all_pets():
    # check the method of the request
    if request.method == 'GET':
        pets = Pet.query.all()
        return [pet.to_dict() for pet in pets], 200
    elif request.method == 'POST':
        # get json data from the web request
        data = request.get_json()

        # can validate data if we choose
        if 'name' not in data:
            return {'error': 'name is required'}, 400

        # build a new pet obj using info from json data
        new_pet = Pet(
            name=data.get('name'),
            age=data.get('age'),
            type=data.get('type')
        )

        # save to db
        db.session.add(new_pet)
        db.session.commit()

        # send a response
        return new_pet.to_dict(), 201


@app.route('/pets/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def pet_by_id(id):
    # query the db for the target pet
    pet = Pet.query.filter(Pet.id == id).first()

    # return 404 if pet doesn't exist
    if pet is None:
        return {'error': 'pet not found'}, 404
    
    if request.method == 'GET':
        return pet.to_dict(), 200
        # return make_response(jsonify(pet_to_dict()), 200)
    elif request.method == 'PATCH':
        # grab data from web request
        data = request.get_json()

        # update the pet (option A)
        if 'name' in data:
            pet.name = data['name']
        if 'age' in data:
            pet.age = data['age']
        if 'type' in data:
            pet.type = data['type']

        # option B
        for field in data:
            # pet.field = data[field]  # doesn't work!
            setattr(pet, field, data[field])  # does work

        # save back to db
        db.session.add(pet)
        db.session.commit()

        # return a response
        return pet.to_dict(), 200
    elif request.method == 'DELETE':
        # delete pet from db
        db.session.delete(pet)
        db.session.commit()

        # return a reponse
        return {}, 204
