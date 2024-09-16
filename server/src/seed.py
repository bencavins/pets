from models import db, Pet
from app import app


def run():
    # delete all pet data
    Pet.query.delete()

    # create some pet objects
    pets = [
        Pet(name='fido', age=3, type='dog'),
        Pet(name='rex', age=6, type='dog'),
        Pet(name='angie', age=13, type='cat'),
        Pet(name='tweety', age=3, type='bird'),
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
