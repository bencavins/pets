from models import db, Pet, Owner
from app import app


def run():
    # delete all pet data
    Pet.query.delete()
    Owner.query.delete()

    # add a couple owners
    alice = Owner(name='alice')
    bob = Owner(name='bob')

    db.session.add_all([alice, bob])
    db.session.commit()

    # create some pet objects
    pets = [
        Pet(name='fido', age=3, type='dog', owner=alice),
        Pet(name='rex', age=6, type='dog', owner=bob),
        Pet(name='angie', age=13, type='cat', owner=bob),
        Pet(name='tweety', age=3, type='bird', owner=alice),
    ]

    # add all pets to the session
    db.session.add_all(pets)
    # for pet in pets:
    #     db.session.add(pet)
    
    # commit changes
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():  # running out script inside and app context
        run()
