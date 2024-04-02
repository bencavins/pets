"""
To create db:

flask db init  # creates the migration folder (only need to run this once)
flask db migrate -m 'some message'  # creates the revision file
flask db upgrade  # apply db changes from revision file
"""


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))




class Dog(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    breed = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # needs to be tablename.colname as a string

    # relationship between Dog -> Owner
    owner = db.relationship('Owner', back_populates='dogs')

    def __repr__(self) -> str:
        return f"<Dog {self.name} {self.age}>"


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # relationship between Owner -> Dog
    dogs = db.relationship('Dog', back_populates='owner')

    def __repr__(self) -> str:
        return f"<Owner {self.name}>"