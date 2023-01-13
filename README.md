# Django-based app for market

### Users can create their adds, choose categories and sell their stuff

## How to run the app

Create virtual environment:
```
python3 -m venv venv
```
```
venv/Scripts/activate (Windows)
source venv/bin/activate (MacOS)
```
### Install requirements:
```
poetry install
```
### Preparing django project:

* Run docker desktop on you PC

* Go to web_market_postgres directory: ```cd web_market_postgres```

* Run in terminal: ```docker-compose up -d```

* Create tables in DB: ```python3 manage.py migrate``` (from web_marker_django directory)

* Fill the DB tables with data: ```python3 manage.py loadall```

### The result should be:
```
Installed 5 object(s) from 1 fixture(s)
Installed 10 object(s) from 1 fixture(s)
Installed 10 object(s) from 1 fixture(s)
Installed 20 object(s) from 1 fixture(s)
```
## Project models

* Ad - model of publication unit.
* Category - category unit
* User - user unit (roles: user, moderator, admin)
* Location - location unit(user location)

## API's endpoints

* 'cat/' - Category model endpoints
* 'ad/' - Ad model endpoints
* 'user/' - User model endpoints
* '' - welcome page
* 'admin/' - django admin panel
