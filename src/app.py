"""
Can start the app with this command: 
flask --debug --app src/app.py run --port 5555

Can also set environment variables:
export FLASK_APP=src/app.py
export FLASK_DEBUG=1
export FLASK_RUN_PORT=5555
flask run

You can also put those environment variables in a .env file
You need to install python-dotenv for this to work
If you do this, add .env to your .gitignore file!


CRUD
Create (POST)
Read (GET)
Update
Delete
"""

from flask import Flask, request
from flask_migrate import Migrate
from models import db, Dog


# initialize flask app
app = Flask(__name__)
# tell sqlalchemy how to connect to our db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# add sqlalchemy plugin
db.init_app(app)
# add the alembic plugin
migrate = Migrate(app, db)


@app.route('/')
def get_root():
    return "<h1>Hello</h1>", 200

@app.route('/dogs', methods=['GET', 'POST'])
def all_dogs():
    if request.method == 'GET':
        # query for all dogs in db
        all_dogs = Dog.query.all()
        # serialize all dogs (turn them into a dictionary)
        results = []
        for dog in all_dogs:
            results.append(dog.to_dict())
        # return the serialized dogs in a response
        return results, 200
    elif request.method == 'POST':
        # get json data from request
        json_data = request.get_json()
        # build new Dog obj
        new_dog = Dog(
            name=json_data.get('name'),
            age=json_data.get('age'),
            breed=json_data.get('breed')
        )
        # save new dog in db
        db.session.add(new_dog)
        db.session.commit()
        # serialize the new dog and return a response
        return new_dog.to_dict(), 201

@app.route('/dogs/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def get_dog_by_id(id):
    # query db for the dog with this id
    dog = Dog.query.filter(Dog.id == id).first()
    # if dog does not exist, return a 404
    if dog is None:
        return {'error': 'dog not found'}, 404
    # check which request method was sent
    if request.method == 'GET':
        # serialize the dog and return a response
        return dog.to_dict(), 200
    elif request.method == 'DELETE':
        # delete the dog from the db
        db.session.delete(dog)
        db.session.commit()
        # return a response with and empty body
        return {}, 204
    elif request.method == 'PATCH':
        # get json data from the request
        json_data = request.get_json()

        # method 1
        # if 'name' in json_data:
        #     dog.name = json_data.get('name')
        # if 'age' in json_data:
        #     dog.age = json_data.get('age')
        # if 'breed' in json_data:
        #     dog.breed = json_data.get('breed')

        # method 2 (a little better)
        # loop through the fields in the request json
        for field in json_data:
            # dog.key = json_data.get(key)  # this is what we want to do
            # set the corresponding attribute on the dog object
            setattr(dog, field, json_data[field])
        # save the updated dog to the db
        db.session.add(dog)
        db.session.commit()
        # serialize the dog and return a response
        return dog.to_dict(), 200
