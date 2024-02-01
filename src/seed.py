import random

from faker import Faker

from app import app
from models import db, Dog, Owner


faker = Faker()
breeds = [
    'bulldog', 
    'collie', 
    'bloodhound', 
    'scottish terrier', 
    'yorkshire terrier',
    'jack russel terrier',
    'poodle',
    'pitbull',
    'great dane',
    'huskey'
]


def create_dogs(owners):
    dogs = []
    for _ in range(20):
        random_owner = random.choice(owners)
        dog = Dog(
            name=faker.first_name(), 
            age=random.randint(0, 15),
            breed=random.choice(breeds),
            owner_id=random_owner.id
        )
        dogs.append(dog)
    return dogs


def create_owners():
    owners = []
    for _ in range(7):
        owner = Owner(name=faker.name())
        owners.append(owner)
    return owners


if __name__ == "__main__":
    with app.app_context():
        print('Clearing db...')
        Dog.query.delete()
        Owner.query.delete()

        print('Seeding owners...')
        owners = create_owners()
        db.session.add_all(owners)
        db.session.commit()

        print('Seeding dogs...')
        dogs = create_dogs(owners)
        db.session.add_all(dogs)

        db.session.commit()

    print('Done!')