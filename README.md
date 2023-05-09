# Backend Setup #

#### Create a `virtual environment` for the project by entering the following commands: ####
`pip3 install virtualenv`
`virtualenv DjangoQuiz`
`source DjangoQuiz/bin/activate`

#### Install Requirements ####
`pip install -r requirements.txt`

#### Create SuprerUser ####
`python manage.py createsuperuser`

#### then run these three commands ####
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`


#### Paste this URL into your browser: ####
`http://127.0.0.1:8000/`


