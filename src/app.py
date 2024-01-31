"""
Can start the app with this command: 
flask --debug --app src/app.py run --port 5555

Can also set environment variables:
export FLASK_APP=src/app.py
export FLASK_DEBUG=1
export FLASK_RUN_PORT=5555
flask run


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
        all_dogs = Dog.query.all()
        results = []
        for dog in all_dogs:
            results.append(dog.to_dict())
        return results, 200
    elif request.method == 'POST':
        # get json data from request
        json_data = request.get_json()
        # build new Dog obj
        new_dog = Dog(
            name=json_data.get('name'),
            age=json_data.get('age'),
            breed=json_data['breed']
        )
        # save new dog in db
        db.session.add(new_dog)
        db.session.commit()
        return new_dog.to_dict(), 201

@app.route('/dogs/<int:id>')
def get_dog_by_id(id):
    dog = Dog.query.filter(Dog.id == id).first()

    if dog is None:
        return {'error': 'dog not found'}, 404

    return dog.to_dict(), 200


