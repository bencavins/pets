# our main flask app
# API == Application Program Interface

# can start flask with
# flask --app src/app.py run --port 5555 --debug

# can also use env vars (don't commit the .env file!!!)
# export FLASK_APP=src/app.py
# export FLASK_RUN_PORT=5555
# export FLASK_DEBUG=1
# flask run


# CRUD == Create, Read, Update, Delete
# HTTP verbs: POST, GET, PATCH (PUT), DELETE
# ReST

from flask import Flask, request, make_response, jsonify
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


@app.route('/dogs')
def dogs():
    # query db for all dog pets
    all_dogs = Pet.query.filter(Pet.type == 'dog').all()
    all_dog_dicts = [d.to_dict() for d in all_dogs]  # turn all dog objs into dicts
    return all_dog_dicts, 200


@app.route('/pets', methods=['GET', 'POST'])
def all_pets():
    if request.method == 'GET':
        pets = Pet.query.all()
        return [p.to_dict() for p in pets], 200
    elif request.method == 'POST':
        # grab json data from request (as dict)
        data = request.get_json()

        # build new pet obj
        try:  # try to run this block of code
            new_pet = Pet(
                name=data.get('name'),
                age=data.get('age'),
                type=data.get('type'),
                owner_id=data.get('owner_id')
            )
        except ValueError as e:
            # if a ValueError is raise above, run this code
            return {'error': str(e)}, 400

        # save new pet obj to the db
        db.session.add(new_pet)
        db.session.commit()

        return new_pet.to_dict(), 201


@app.route('/pets/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()

    if not pet:
        return {'error': 'pet not found'}, 404
    
    if request.method == 'GET':
        return pet.to_dict(), 200
    elif request.method == 'PATCH':
        # get json data from request
        data = request.get_json()

        # option 1, check every single field
        # if 'name' in data:
        #     pet.name = data['name']
        # if 'age' in data:
        #     pet.age = data['age']
        # if 'type' in data:
        #     pet.type = data['type']

        # option 2, loop through json keys and use setattr to update the attribute on the object
        for field in data:
            # pet.field = data[field]  # this doesn't work
            try:
                setattr(pet, field, data[field])
            except ValueError as e:
                return {'error': str(e)}, 400


        db.session.add(pet)
        db.session.commit()

        return pet.to_dict(), 200
    elif request.method == 'DELETE':
        db.session.delete(pet)
        db.session.commit()

        return {}, 204