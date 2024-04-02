import random
from app import app
from models import db, Dog, Owner


def run():
    # delete all dogs from dogs table
    print('deleting all data...')
    Dog.query.delete()
    Owner.query.delete()

    print('adding owners...')
    owners = [
        Owner(name='joe'),
        Owner(name='anne')
    ]
    db.session.add_all(owners)
    db.session.commit()  # db will set owner.id right here

    # add some test dogs
    print("adding dogs...")
    dogs = [
        Dog(name='fido', age=3, breed='bulldog', owner=owners[0]),
        Dog(name='rex', age=2, breed='poodle', owner=owners[0]),
        Dog(name='gus', age=14, breed='terrier', owner=owners[1]),
    ]
    db.session.add_all(dogs)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        run()
