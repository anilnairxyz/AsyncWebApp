# AsyncWebApp
A Flask Web App using Celery and RedisQ / RabbitMQ

## Method 1: Use Redis as the broker
* Install Redis
* Run the redis-server (default port 6379)
```redis-server```
* Run the app using the redis configuration
```python app.py```
* Invoke the celery worker
```celery worker -A app.celery --loglevel=info```
* curl to test the application

## Method 2: Use RabbitMQ as the broker
* Download and run the docker container for rabbit. Here we use this one:
  ```docker run -d -p 5672:5672 -p 15672:15672  --name rabbitmq rabbitmq:3-management```
* Run the app using rabbit configuration
```python app.py```
* Invoke the celery worker
```celery worker -A app.celery --loglevel=info```
* curl to test the app

