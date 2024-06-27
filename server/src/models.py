'''
Flask Migrate Commands

flask db init  # set up migration folder
flask db migrate -m ''  # generate revision file
flask db upgrade  # upgrade to latest revision


>>> Pet
<class 'models.Pet'>
>>> Pet.query
<flask_sqlalchemy.query.Query object at 0x1101e68c0>
>>> Pet.query.all()
[<Pet fido 3 dog>, <Pet felix 10 cat>, <Pet rex 4 dog>]
>>> Pet.query.filter(Pet.type == 'dog')
<flask_sqlalchemy.query.Query object at 0x110230cd0>
>>> Pet.query.filter(Pet.type == 'dog').all()
[<Pet fido 3 dog>, <Pet rex 4 dog>]
>>> Pet.query.filter(Pet.type == 'dog').first()
<Pet fido 3 dog>
>>> Pet.query.filter(Pet.id == 1).first()
<Pet fido 3 dog>
>>> Pet.query.filter(Pet.id == 99).first()
>>>
'''

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


db = SQLAlchemy(metadata=MetaData(naming_convention=convention))


class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    type = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    owner = db.relationship('Owner', back_populates='pets')

    serialize_rules = ['-owner.pets']  # prevents recursive loop

    @validates('age')
    def validates_not_negative(self, key, new_value):
        if new_value < 0:
            # raise error if validation fails
            raise ValueError(f'{key} cannot be negative')
        # return value if valdation passes
        return new_value
    
    @validates('name')
    def validates_not_empty(self, key, new_value):
        if new_value is None or len(new_value) == 0:
            raise ValueError(f'{key} cannot be empty')
        return new_value

    # to_dict() gets added by SerializerMixin
    # def to_dict(self):
    #     return {
    #         'name': self.name,
    #         'age': self.age,
    #         'type': self.type
    #     }

    def __repr__(self) -> str:
        return f"<Pet {self.name} {self.age} {self.type}>"


class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pets = db.relationship('Pet', back_populates='owner')

    serialize_rules = ['-pets.owner']  # prevents recursive loop

    def __repr__(self) -> str:
        return f"<Owner {self.name}>"
