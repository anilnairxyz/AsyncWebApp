# AsyncWebApp
A Flask Web App using Celery and RedisQ / RabbitMQ

## Method 1: Use Redis as the broker
* Install Redis
* Run the redis-server (default port 6379)
* Run the app using the redis configuration
* Invoke the celery worker
* curl to test the application

## Method 2: Use RabbitMQ as the broker
