import os

from flask import Flask, request, session
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Dog, Owner, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY')
db.init_app(app)
migrate = Migrate(app, db)
cors = CORS(app, supports_credentials=True)
# cors = CORS(app)


@app.route('/')
def root():
    return "<h1>Hello world!</h1>"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter(User.username == data.get('username')).first()

    if not user:
        return {'error': 'user not found'}, 404
    
    if not user.authenticate(data.get('password')):
        return {'error': 'invalid password'}, 401
    
    session['user_id'] = user.id
    print(session)
    return user.to_dict(), 201

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(username=data.get('username'))
    new_user.password_hash = data.get('password')
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict(), 201

@app.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    print(session)
    return {}, 204

@app.route('/authorized')
def is_authorized():
    print(session)
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()

    if not user:
        return {'error': 'not authorized'}, 401
    
    return user.to_dict(), 200

@app.route('/dogs', methods=['GET', 'POST'])
def get_all_dogs():
    print(session)
    if request.method == 'GET':
        dogs = Dog.query.all()
        return [dog.to_dict() for dog in dogs], 200
    elif request.method == 'POST':
        dog_json = request.get_json()
        try:
            new_dog = Dog(
                name=dog_json.get('name'),
                age=dog_json.get('age'),
                owner_id=dog_json.get('owner_id')
            )
        except ValueError as e:
            return {'error': str(e)}, 400
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

@app.route('/owners')
def get_all_owners():
    owners = Owner.query.all()
    return [owner.to_dict() for owner in owners], 200


@app.route('/owners/<int:id>')
def get_owner_by_id(id):
    owner = Owner.query.filter(Owner.id == id).first()
    if not owner:
        return {'error': 'owner not found'}, 404
    else:
        return owner.to_dict(), 200
