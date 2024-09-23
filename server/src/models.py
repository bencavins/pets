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
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property



class PetException(Exception):
    pass


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

# init bcrypt plugin
bcrypt = Bcrypt()


# create a new class/model
class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'  # tablename is required

    __table_args__ = (db.CheckConstraint('age >= 0', name='ck_age_not_neg'), )

    # define columns on our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    type = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # fk for owners.id

    # relationship needs the class name (as a str)
    owner = db.relationship('Owner', back_populates='pets')

    # serialization rules
    serialize_rules = ('-owner.pets',) # -owner_id is optional
    # serialize_only = ['name']

    @validates('age')
    def validates_age(self, key, new_age):
        if new_age < 0:
            raise PetException('age cannot be negative')
        return new_age  # similar to self._age = new_age

    def __repr__(self) -> str:
        return f'<Pet {self.id} {self.name} {self.age}>'
    

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    pets = db.relationship('Pet', back_populates='owner')

    serialize_rules = ['-pets.owner']

    def __repr__(self) -> str:
        return f'<Owner {self.id} {self.name}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String)

    serialize_rules = ['-password_hash']

    @hybrid_property
    def password(self):
        """Returns the password hash"""
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        """Hashes the plain text password"""
        bytes = plain_text_password.encode('utf-8')  # convert our string into raw bytes
        self.password_hash = bcrypt.generate_password_hash(bytes)  # hash the bytes

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self.password_hash,  # hashed password
            password.encode('utf-8')  # plain text password
        )

    def __repr__(self) -> str:
        return f'<User {self.id} {self.username}>'

