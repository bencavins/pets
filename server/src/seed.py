from models import db, Pet, Owner
from app import app
import requests


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
    # pets = [
    #     Pet(name='fido', age=3, type='dog', owner=owners[0]),
    #     Pet(name='felix', age=10, type='cat', owner=owners[1]),
    #     Pet(name='rex', age=4, type='dog', owner=owners[0])
    # ]
    # db.session.add_all(pets)
    # db.session.commit()

    # from pprint import pprint
        
    # we can get data from another api if we want to
    data = requests.get('https://pokeapi.co/api/v2/generation/1').json()

    # import time
    for pk in data['pokemon_species']:
        # time.sleep(1)
        pk_data = requests.get(pk['url']).json()
        new_pet = Pet(name=pk['name'], type=pk_data['color']['name'])
        db.session.add(new_pet)
    db.session.commit()
    


if __name__ == '__main__':
    with app.app_context():
        run()
