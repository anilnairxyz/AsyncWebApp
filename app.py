# -*- coding: utf-8 -*-
"""
A flask web service API that:
runs a dummy task on celery that takes a reasonable long time
responds with 202 and the poll link
updates progress on the poll link
Includes configs for Redis broker
"""
from flask import Flask, request, jsonify, make_response
import time
from celery import Celery

app = Flask(__name__)


# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task(bind=True)
def analyze_task(self):
    """Long running task run in the background using celery
    """
    loops = 20
    for i in range(loops):
        self.update_state(state='PENDING', meta={'progress': i*100/loops})
        time.sleep(1)
    return {'progress': 100}


@app.errorhandler(404)
def url_not_found(error):
    """
    Custom JSON error handler for 404 response
    """
    response = {'status': 404, 'message': 'URL not found'}
    return make_response(jsonify(response), 404)


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Custom JSON error handler for 405 response
    """
    response = {'status': 405, 'message': 'Method not allowed'}
    return make_response(jsonify(response), 405)


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    """
    Basic healthcheck
    """
    response = {'status': 200, 'message': 'Connection fine'}
    return make_response(jsonify(response), 200)


@app.route("/analyze", methods=['GET'])
def analyze():
    """
    Start a background thread to run long running task
    Return an accepted response
    """
    task = analyze_task.apply_async()
    response = ({'status': 202, 'message': 'Analyze Request Accepted',
                 'location': '/status/'+str(task.id)})
    return make_response(jsonify(response), 202)


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = analyze_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'status': 200, 'progress': task.info.get('progress', 0)}
        return make_response(jsonify(response), 200)
    elif task.state != 'FAILURE':
        response = {'status': 303, 'progress': task.info.get('progress', 100)}
        return make_response(jsonify(response), 303)
    else:
        response = {'status': 500, 'progress': 0}
        return make_response(jsonify(response), 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
