from flask import Flask
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

@app.route('/pets')
def get_pets():
    # TODO get pets from db
    pets = [
        {
            'id': 1,
            'name': 'fido'
        },
        {
            'id': 2,
            'name': 'rex'
        }
    ]
    return pets, 200

@app.route('/pets/<int:id>')
def get_pet_by_id(id):
    return f"<h1>You selected pet id == {id}</h1>"

