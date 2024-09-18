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
from sqlalchemy import MetaData


# naming convention for db constraints (fixes an alembic bug)
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


# init sqlalchemy object
db = SQLAlchemy(metadata=MetaData(naming_convention=convention))


# create a new class/model
class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'  # tablename is required

    # define columns on our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    type = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # fk for owners.id

    # relationship needs the class name (as a str)
    owner = db.relationship('Owner', back_populates='pets')

    # serialization rules
    serialize_rules = ['-owner.pets', '-owner_id']  # -owner_id is optional

    def __repr__(self) -> str:
        return f'<Pet {self.id} {self.name} {self.age}>'
    

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pets = db.relationship('Pet', back_populates='owner')

    serialize_rules = ['-pets.owner']

    def __repr__(self) -> str:
        return f'<Owner {self.id} {self.name}>'

