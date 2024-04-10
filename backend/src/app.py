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
import os

from flask import Flask, request, session
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Dog, User, Owner


app = Flask(__name__)
# set the db connection string
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set a secret key (needed for browser cookies)
app.secret_key = os.environ['SECRET_KEY']

# initialize the sqlalchemy db
db.init_app(app)
# initialize alembic (migration framework)
Migrate(app, db)
# initialize CORS
CORS(app, supports_credentials=True)


@app.route("/")
def root():
    return '<h1>HELLO</h1>'

@app.route('/helloworld')
def hello_world():
    return {'message': 'goodbye world!'}

# login
@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()

    # check that user exists
    user = User.query.filter(User.username == json_data.get('username')).first()
    if not user:
        return {'error': 'user not found'}, 404
    
    # check the user's password
    if not user.authenticate(json_data.get('password')):
        return {'error': 'login failed'}, 401
    
    # store a cookie in the browser
    session['user_id'] = user.id

    # return a response
    return user.to_dict(), 200

# logout
@app.route('/logout', methods=['DELETE'])
def logout():
    # delete the user_id cookie
    session.pop('user_id', None)
    return {}, 204

# signup
@app.route('/signup', methods=['POST'])
def signup():
    # get the json data
    json_data = request.get_json()

    user = User.query.filter(User.username == json_data.get('username')).first()
    if user:
        return {'error': 'user already exists'}, 400

    # create a new user
    new_user = User(
        username=json_data.get('username'),
        password=json_data.get('password'),
    )

    # add to db
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict(), 201

# check_session (is user currently logged in?)
@app.route('/check_session', methods=['GET'])
def check_session():
    # get user id from the browser cookies
    user_id = session.get('user_id')

    # query the db to make sure that user id is valid
    user = User.query.filter(User.id == user_id).first()

    # if the user isn't valid, send error
    if not user:
        return {'error': 'unauthorized'}, 401
    else:
        return user.to_dict(), 200

@app.route('/dogs', methods=['GET', 'POST'])
def all_dogs():
    if request.method == 'GET':
        # query db for all dog objs
        dog_objs = Dog.query.all()

        # map every dog obj to a dog dict
        dog_dicts = []
        for dog in dog_objs:
            dog_dicts.append(dog.to_dict())

        return dog_dicts, 200
        # can do this whole thing in one line
        # return [dog.to_dict() for dog in Dog.query.all()], 200
    elif request.method == 'POST':
        # get the json data from the request body
        json_data = request.get_json()

        # build new dog obj using info from json_data
        try:
            new_dog = Dog(
                name=json_data.get('name'),
                age=json_data.get('age'),
                breed=json_data.get('breed'),
                owner_id=json_data.get('owner_id')
            )
        except ValueError as e:
            return {'error': str(e)}, 400

        # save to db
        db.session.add(new_dog)
        db.session.commit()

        # we NEED to return a response
        return new_dog.to_dict(), 201

@app.route('/dogs/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def dog_by_id(id):
    # query db for the matching dog object
    dog_obj = Dog.query.filter(Dog.id == id).first()

    # check if the dog_obj exists
    if dog_obj is None:
        return {'error': 'dog not found'}, 404
    
    if request.method == 'GET':
        # return a response (serialize the dog object to a dict)
        return dog_obj.to_dict(), 200
    elif request.method == 'DELETE':
        # delete dog from the db
        db.session.delete(dog_obj)
        db.session.commit()

        # we NEED to return a response
        return {}, 204
    elif request.method == 'PATCH':
        # get the json data from the request
        json_data = request.get_json()

        # update the dog obj with the new data
        # approach #1 (a little annoying)
        # if 'name' in json_data:
        #     dog_obj.name = json_data.get('name')
        # if 'age' in json_data:
        #     dog_obj.age = json_data.get('age')
        # if 'breed' in json_data:
        #     dog_obj.breed = json_data.get('breed')
        # if 'owner_id' in json_data:
        #     dog_obj.owner_id = json_data.get('owner_id')

        # approach #2 (less annoying)
        for field in json_data:
            value = json_data[field]
            # dog_obj[field] = value  # this doesn't work
            setattr(dog_obj, field, value)
        
        # save dog obj back to the db
        db.session.add(dog_obj)
        db.session.commit()

        # return a response
        return dog_obj.to_dict(), 200

@app.route('/owners', methods=['GET'])
def all_owners():
    return [owner.to_dict() for owner in Owner.query]
    
@app.route('/owners/<int:id>', methods=['GET'])
def owner_by_id(id):
    owner = Owner.query.filter(Owner.id == id).first()
    
    if not owner:
        return {'error': 'owner not found'}, 404
    
    return owner.to_dict(), 200
    