from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin


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
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    owner = db.relationship('Owner', back_populates='dogs')

    serialize_rules = ('-owner.dogs',)

    __table_args__ = (
        db.CheckConstraint('age >= 0', 'age_not_neg')
    ,)

    @validates('name')
    def validate_name(self, key, new_name):
        if len(new_name) == 0:
            raise ValueError('name must contain at least 1 character')
        return new_name
        
    @validates('age')
    def validate_age(self, key, new_age):
        if new_age < 0:
            raise ValueError('age cannot be negative')
        return new_age

    def __repr__(self) -> str:
        return f"<Dog name: {self.name}, id: {self.id}>"
    

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    dogs = db.relationship('Dog', back_populates='owner')

    serialize_rules = ('-dogs.owner',)

    def __repr__(self) -> str:
        return f"<Owner {self.name}>"


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)

    serialize_rules = ('-_password_hash',)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"
