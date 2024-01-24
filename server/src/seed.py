import random

from faker import Faker

from app import app
from models import db, Dog


faker = Faker()


def create_dogs():
    dogs = []
    for _ in range(20):
        dog = Dog(name=faker.first_name(), age=random.randint(0, 15))
        dogs.append(dog)
    return dogs


if __name__ == "__main__":
    with app.app_context():
        print('Clearing db...')
        Dog.query.delete()

        print('Seeding dogs...')
        dogs = create_dogs()
        db.session.add_all(dogs)
        db.session.commit()

    print('Done!')