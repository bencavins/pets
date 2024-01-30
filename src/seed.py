from app import app
from models import db, Dog


if __name__ == '__main__':
    with app.app_context():
        # delete all dogs
        Dog.query.delete()

        dog = Dog(name='fido', age=3, breed='terrier')
        db.session.add(dog)
        dog2 = Dog(name='rex', age=6, breed='bulldog')
        db.session.add(dog2)
        
        db.session.commit()