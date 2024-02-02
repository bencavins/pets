"""
SQLAlchemy -- generates SQL for DB

Alembic -- DB Migration tool
flask db init -- initializes the migration folder
flask db migrate -m 'some message' -- creates the upgrade script
flask db upgrade -- runs our upgrade scripts


Relationships need to be defined on both sides:
Dog:
    owner = db.relationship('Owner', back_populates='dogs')
Owner:
    dogs = db.relationship('Dog', back_populates='owner')

"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


# naming conventions (helps with albemic bug)
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=convention))

class Dog(db.Model, SerializerMixin):
    __tablename__ = 'dogs'

    # ('-relationshiop_name.back_populates',)
    serialize_rules = ('-owner.dogs',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) # this means required
    age = db.Column(db.Integer)
    breed = db.Column(db.String)
    # need to tell SQLAlchemy which table/column this FK references (table.col)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    __table_args__ = (
        db.CheckConstraint('age >= 0', 'age_not_neg')
    ,)

    @validates('age')
    def validate_age(self, key, new_age):
        """this code will run every time age is set on our Dog"""
        # key == the name of the field we are currently validating
        if new_age < 0:
            raise ValueError('age cannot be negative')
        return new_age

    # add owner attribute (define the relationship)
    owner = db.relationship('Owner', back_populates='dogs')

    def __repr__(self) -> str:
        return f"<Dog {self.name}>"
    
    # def to_dict() gets added by SerializerMixin

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    serialize_rules = ('-dogs.owner',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    # add dogs attribute (define the relationship)
    dogs = db.relationship('Dog', back_populates='owner')

    def __repr__(self) -> str:
        return f"<Owner {self.name}>"