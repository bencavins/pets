# pets

## Intro to Flask
- [ ] install `flask`
- [ ] create simple `app.py`
- [ ] show how to run app
- [ ] build some basic routes (with params)
- [ ] add `.env` file for simplicity (need to install python-dotenv) and `.gitignore`

## SQLAlchemy & Alembic
- [ ] install `flask-sqlalchemy`
- [ ] set up `models.py` with Dog class
- [ ] install `flask-migrate`, setup alembic and SQLAlchemy
  - [ ] use a better file template (file_template = %%(year)04d-%%(month)02d-%%(day)02d_%%(hour)02d-%%(minute)02d-%%(second)02d_%%(rev)s_%%(slug)s)
  - [ ] add the naming convention
- [ ] run `flask db init`, `flask db migrate`, `flask db upgrade`
- [ ] add dogs and query dogs with flask shell
- [ ] write a seed script
  - [ ] can optionally install `faker`

## APIs
- [ ] create a /dogs route
- [ ] add serializer for Dog (install `sqlalchemy-serializer`)
- [ ] demo POSTman
- [ ] create a /dogs/<int:id> route
  - [ ] test for 404s
- [ ] allow POST to /dogs
- [ ] add DELETE
- [ ] add PATCH

## Constraints/Validations
- [ ] Make Dog name required (discuss `nullable` and `unique`)
- [ ] Create a custom constraint for age (cannot be neg)
- [ ] Add validation for name and age

## Relationships
- [ ] add Owner class
- [ ] add fk to Owner on Dog
- [ ] rewrite seed script
  - [ ] *tricky* talk about when ids get added
- [ ] add relationship
- [ ] add serialize_rules
- [ ] add route for owners

## Adding the Front-End
- [ ] create a simple react app with vite
  - [ ] run `npm create vite@latest`
  - [ ] run `npm react-router-dom`
- [ ] set up a fetch
- [ ] add CORS
- [ ] set up form POST (with error handling)

## Auth
- [ ] create a User class