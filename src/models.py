"""
SQLAlchemy -- generates SQL for DB

Alembic -- DB Migration tool
flask db init -- initializes the migration folder
flask db migrate -m 'some message' -- creates the upgrade script
flask db upgrade -- runs our upgrade scripts
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# naming conventions (helps with albemic bug)
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

    def __repr__(self) -> str:
        return f"<Dog {self.name}>"
