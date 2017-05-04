# fööt
E-commerce "deal a day" web application built in Python/Django. A clone of woot.com created from start to finish in a 5 day sprint.

## Authors
  * [Mick Johnson](https://github.com/mickajohnson)
  * [Michael Mitchell](https://github.com/mikeybags)
  * [Curtis Wulfsohn](https://github.com/cwulfsohn)

## Technologies
  * Python
  * Django
  * JQuery
  * SQLite3
  
## Demo
* [AWS Deployed Demo Site](http://54.187.237.150/)

## Dependencies
  ```
    bcrypt==3.1.2
    cffi==1.9.1
    Django==1.10.5
    django-extensions==1.7.5
    olefile==0.44
    Pillow==4.0.0
    pycparser==2.17
    pyparsing==2.1.10
    pytz==2016.10
    six==1.10.0
 ```
## To Run Project Locally

* Clone the project
  ```
    git clone https://github.com/mikeybags/woot.git
  ```
* Move into project directory
  ```
    cd woot
  ```
* Create and start a a virtual environment
  ```
    virtualenv env --no-site-packages
    source env/bin/activate
  ```
* Install project dependencies
  ```
    pip install -r requirements.txt
  ```
* Migrate
  ```
    python manage.py migrate
  ```
* Start the server
  ```
    python manage.py runserver
  ```
* Open localhost:8000 on your browser to view the app
