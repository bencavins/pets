# pets

## Intro to Flask
- [x] install `flask`
- [x] create simple `app.py`
- [x] show how to run app
- [x] build some basic routes (with params)
- [x] add `.env` file for simplicity (need to install python-dotenv) and `.gitignore`

## SQLAlchemy & Alembic
- [x] install `flask-sqlalchemy`
- [x] set up `models.py` with Dog class
- [x] install `flask-migrate`, setup alembic and SQLAlchemy
  - [x] use a better file template (file_template = %%(year)04d-%%(month)02d-%%(day)02d_%%(hour)02d-%%(minute)02d-%%(second)02d_%%(rev)s_%%(slug)s)
  - [x] add the naming convention
- [x] run `flask db init`, `flask db migrate`, `flask db upgrade`
- [x] add dogs and query dogs with flask shell
- [x] write a seed script
  - [x] can optionally install `faker`

## APIs
- [x] create a /dogs route
- [x] add serializer for Dog (install `sqlalchemy-serializer`)
- [x] demo POSTman
- [x] create a /dogs/<int:id> route
  - [x] test for 404s
- [x] allow POST to /dogs
- [x] add DELETE
- [x] add PATCH

## Constraints/Validations
- [x] Make Dog name required (discuss `nullable` and `unique`)
- [x] Create a custom constraint for age (cannot be neg)
- [x] Add validation for name and age

## Relationships
- [x] add Owner class
- [x] add fk to Owner on Dog
- [x] rewrite seed script
  - [ ] *tricky* talk about when ids get added
- [x] add relationship
- [x] add serialize_rules
- [ ] add route for owners

## Adding the Front-End
- [x] create a simple react app with vite
  - [x] run `npm create vite@latest`
  - [x] run `npm react-router-dom`
- [x] set up a fetch
- [x] add CORS
- [x] set up form POST (with error handling)

## Auth
- [ ] create a User class