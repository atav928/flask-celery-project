"""Setup"""
from celery.result import AsyncResult
from flask import jsonify, request
from project import create_app, ext_celery
from project.users.tasks import celery_commit_all


app = create_app()
celery = ext_celery.celery


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/commit', methods=['POST'])
def commit():
    tsg_id = str(request.args.get('tsg_id', ""))
    client_id = request.authorization.username
    client_secret = request.authorization.password
    tasks = celery_commit_all.delay(tsg_id=tsg_id, client_id=client_id,
                                    client_secret=client_secret, verify=True)
    return jsonify({'task_id': tasks.task_id, 'state': tasks.state})


@app.route('/task/<task_id>', methods=['GET'])
def get_task(task_id):
    tasks = AsyncResult(task_id)
    return jsonify({'task_id': tasks.task_id, 'state': tasks.state, "results": tasks.result})
