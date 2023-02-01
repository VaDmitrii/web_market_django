# Web market backend

### Users can create their adds, choose categories and sell their products or services.

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
* Selection - selection of ads liked by User

## API's endpoints

* 'cat/' - Category model endpoints
* 'ad/' - Ad model endpoints
* 'user/' - User model endpoints
* 'selection/' - ads selection each user can create
* '' - welcome page
* 'admin/' - django admin panel
* 'api/schema/swagger-ui/' - API documentaion

## Endpoints use order (Postman)

* 'user/create/' - create new User in PostgreSQL database by providing 'username', 'password', 'email' and 'date_ob_birth'(JSON)
* 'user/token/' - retrieve JWT 'access' and 'refresh' tokens by providing 'username' and 'password' of user created on previous step
* Now you can send CRUD requests to all endpoints of API. More information you can see in API's documentation on 'api/schema/swagger-ui/' endpoint 
