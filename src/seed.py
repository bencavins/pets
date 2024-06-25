from models import db, Pet, Owner
from app import app


def run():
    # delete all rows from pets table
    Pet.query.delete()
    Owner.query.delete()
    db.session.commit()

    # add owners
    owners = [
        Owner(name='joe'),
        Owner(name='anne')
    ]
    db.session.add_all(owners)
    db.session.commit()

    # add pets
    # pets = [
    #     Pet(name='fido', age=3, type='dog', owner_id=owners[0].id),
    #     Pet(name='felix', age=10, type='cat', owner_id=owners[1].id),
    #     Pet(name='rex', age=4, type='dog', owner_id=owners[0].id)
    # ]
    pets = [
        Pet(name='fido', age=3, type='dog', owner=owners[0]),
        Pet(name='felix', age=10, type='cat', owner=owners[1]),
        Pet(name='rex', age=4, type='dog', owner=owners[0])
    ]
    db.session.add_all(pets)
    db.session.commit()

    


if __name__ == '__main__':
    with app.app_context():
        run()
