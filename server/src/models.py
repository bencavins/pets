from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


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

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)

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
