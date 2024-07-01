# our main flask app
# API == Application Programing Interface

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

import os
from flask import Flask, request, make_response, jsonify, session
from models import db, Pet, Owner, User
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']  # how to connect to the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # optional performance thing
app.secret_key = os.environ['SECRET_KEY'] # grab the secret key from env variables


db.init_app(app)  # link sqlalchemy with flask
Migrate(app, db)  # set up db migration tool (alembic)
CORS(app)  # set up cors


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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # get user data

    # check if the user exists
    user = User.query.filter(User.username == data['username']).first()
    if not user:
        return {'error': 'login failed'}, 401
    
    # check if password can generate the same hash
    if not user.authenticate(data['password']):
        return {'error': 'login failed'}, 401
    
    # set browser cookie
    session['user_id'] = user.id

    return user.to_dict(), 200

@app.route('/signup')
def signup():
    pass

@app.route('/logout')
def logout():
    pass

@app.route('/check_session')
def check_session():
    # get the cookie
    user_id = session.get('user_id')

    if not user_id:
        # no cookie set, user is not logged in
        return {'error': 'authorization failed'}, 401
    
    user = User.query.filter(User.id == user_id).first()
    if not user:
        # cookie is invalid
        return {'error': 'authorization failed'}, 401
    
    return {'message': "authorization success"}, 200

@app.route('/pets', methods=['GET', 'POST'])
def all_pets():
    t = get_all_owners()
    print(t[0])
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


@app.get('/owners')  # @app.route('/owners', methods=['GET'])
def get_all_owners():
    owners = Owner.query.all()
    return [o.to_dict() for o in owners], 200

@app.post('/owners') # @app.route('/owners', methods=['POST'])
def post_owner(): 
    pass