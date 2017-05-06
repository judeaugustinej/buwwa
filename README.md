# Buwwa ZERO FOOD WASTAGE

* To minimize food wastage by connecting foodsupplier(Restaurant, Hotels, ...) with NGO(Old age home, Orphanages)

* App selected for savethehacker-2017[http://www.savethehacker.com/] Hackathon.

## App Work Flow

* Foodsupplier or NGO can signup or register.

* Foodsupplier can sponser food by filling-up a SPONSER-FOOD form, as soon as the foodsupplier does that a request is send to NGO as Food available request.

* NGO can request for food by filling-up a NEED-FOOD form, as soon as the NGO does that a request is send to Foodsupplier as NEED-Food request.

## Features

- SMS/Email alert to NGO and Foodsupplier
- Maps to find location of NGO and Foodsupplier for better co-ordination
- Recommendation of food-availablity to NGO
- Recommendation for food-sponsoring to Foodsuppliers
- API for IOS/Andriod/3rd-party apps.

## Code-development-work-flow

* Clone the code
```
git clone https://github.com/judeaugustinej/buwwa.git
```

* Install required packages
```
pip install -r requirements.txt
```

* Run migrations
```
python manage.py migrate
```

* Create a user.
```
python manage.py createsuperuser
```

* Start the app
```
python manage.py runserver
```

## DB-Schema


## Tech-Stack
* Django - Fullstack web-app ie(MVC)
* Django-rest-framework - Rest-api
* Database - PostgresDB
* Deployment - Heroku
* CI-CD - git-travis-Heroku

## Team

* Jude
* sri
* karthick
* 

## TODO
* Seperate UI from Backend.
* Dockerise the app.
* Deploy in aws
* Native iOS/Andriod support

## License: MIT
