from flask import Flask, request
from flask_migrate import Migrate

from models import db, Dog


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def root():
    return "<h1>Hello world!</h1>"

@app.route('/dogs', methods=['GET', 'POST'])
def get_all_dogs():
    if request.method == 'GET':
        dogs = Dog.query.all()
        return [dog.to_dict() for dog in dogs], 200
    elif request.method == 'POST':
        dog_json = request.get_json()
        new_dog = Dog(
            name=dog_json.get('name'),
            age=dog_json.get('age')
        )
        db.session.add(new_dog)
        db.session.commit()
        return new_dog.to_dict(), 201

@app.route('/dogs/<int:id>')
def get_pet_by_id(id):
    dog = Dog.query.filter(Dog.id == id).first()
    if not dog:
        return {'error': 'dog not found'}, 404
    else:
        return dog.to_dict(), 200
