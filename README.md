# auxin
[under development]

Hydro backend

## Install Dependencies
```
pip install -r requirements.txt
```
Currently following this tutorial: https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/

## Running the app
Start celery:
```
celery -A auxin worker --loglevel=info
```
To run a test task run the following in another window:
```
python3 -m auxin.main
```
## Using Flower
Flower is a web-based monitoring system for Celery. To run flower run the following in a new terminal window:
```
celery -A auxin flower
```
Celery will launch a local server at http://localhost:5555