# SQLAlchemy -- Python ORM, maps db rows to python objects
# Alembic (aka Flask Migrate) -- db migration tool

# to use alembic:
# flask db init  # initialize alembic (creates the migration folder) 
# flask db migrate -m 'some message'  # create a revision
# flask db upgrade [optional revision id]  # upgrade our db


"""
add data to db
>>> p1 = Pet(name='fido', age=2, type='dog')
>>> p1
<Pet None fido 2>
>>> db.session.add(p1)
>>> db.session.commit()

query db for all pets
>>> Pet.query.all()
[<Pet 1 fido 2>, <Pet 2 fluffy 5>]

query db for single pet
>>> Pet.query.filter(Pet.name == 'fido').first()
<Pet 1 fido 2>

update a pet
>>> p1 = Pet.query.filter(Pet.id == 2).first()
>>> p1
<Pet 2 fluffy 5>
>>> p1.name = 'rex'
>>> p1
<Pet 2 rex 5>
>>> db.session.add(p1)
>>> db.session.commit()

delete a pet
>>> p1 = Pet.query.filter(Pet.id == 2).first()
>>> p1
<Pet 2 rex 5>
>>> db.session.delete(p1)
>>> db.session.commit()
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


# init sqlalchemy object
db = SQLAlchemy()


# create a new class/model
class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'  # tablename is required

    # define columns on our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    type = db.Column(db.String)

    # to_dict() method gets added by SerializerMixIn
    # def to_dict(self):

    def __repr__(self) -> str:
        return f'<Pet {self.id} {self.name} {self.age}>'
