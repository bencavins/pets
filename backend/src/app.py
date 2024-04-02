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

from flask import Flask
from flask_migrate import Migrate

from models import db


app = Flask(__name__)
# set the db connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the sqlalchemy db
db.init_app(app)
# initialize alembic (migration framework)
Migrate(app, db)


@app.route("/")
def root():
    return '<h1>HELLO</h1>'

@app.route('/helloworld')
def hello_world():
    return {'message': 'goodbye world!'}

@app.route('/user/<int:id>')
def user_by_id(id):
    return {'your user id is': id}