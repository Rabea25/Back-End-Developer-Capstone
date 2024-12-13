using pipenv instead of venv, to run this project run the following in terminal
`pipenv shell`
`pipenv install`
then modify db in settings.py according to what you have locally then
`python manage.py makemigrations`
`python manage.py migrate`

might be python3 for you 

superuser username: admin
superuser password: 123
(or i guess you are you running against your local db so idk)

static index page:
http://127.0.0.1:8000/restaurant/

menu api:
http://127.0.0.1:8000/restaurant/menu
http://127.0.0.1:8000/restaurant/menu/1

booking api:
http://127.0.0.1:8000/restaurant/booking
http://127.0.0.1:8000/restaurant/booking/1

djoser and token obtain

/auth/users
/auth/token/login
/api-token-auth (post request from insomnia with valid username and password)
