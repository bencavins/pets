"""
To create db:

flask db init  # creates the migration folder (only need to run this once)
flask db migrate -m 'some message'  # creates the revision file
flask db upgrade  # apply db changes from revision file
"""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
bcrypt = Bcrypt()



class Dog(db.Model, SerializerMixin):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer)
    breed = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # needs to be tablename.colname as a string

    # relationship between Dog -> Owner
    owner = db.relationship('Owner', back_populates='dogs')

    serialize_rules = ['-owner.dogs']

    @validates('name')
    def validates_not_blank(self, key, new_value):
        if len(new_value) == 0:
            raise ValueError(f'{key} cannot be blank')
        else:
            return new_value
        
    @validates('age')
    def validates_age(self, key, new_age):
        if new_age < 0:
            raise ValueError(f'{key} cannot be negative')
        else:
            return new_age

    # serializer adds this method:
    # def to_dict(self):
    #     return {
    #         'name': self.name,
    #         'age': self.age,
    #     }

    def __repr__(self) -> str:
        return f"<Dog {self.name} {self.age}>"


class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # relationship between Owner -> Dog
    dogs = db.relationship('Dog', back_populates='owner')

    serialize_rules = ['-dogs.owner']

    def __repr__(self) -> str:
        return f"<Owner {self.name}>"
    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password = db.Column(db.String, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        pass_hash = bcrypt.generate_password_hash(new_password.encode('utf-8'))
        self._password = pass_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password, password.encode('utf-8'))
