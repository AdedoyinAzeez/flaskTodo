import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

from datetime import datetime
from flask import request, Response
import json

from .models import Task, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('mysql://localhost:8000/flask_todo')
db = SQLAlchemy(app)

INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'


@app.route('/api/v1', methods=["GET"])
@app.route('/api/v1/', methods=["GET"])

def info_view():
    """List of routes for this API."""
    output = {
        'info': 'GET /api/v1',
        'register': 'POST /api/v1/accounts',
        'single profile detail': 'GET /api/v1/accounts/<username>',
        'edit profile': 'PUT /api/v1/accounts/<username>',
        'delete profile': 'DELETE /api/v1/accounts/<username>',
        'login': 'POST /api/v1/accounts/login',
        'logout': 'GET /api/v1/accounts/logout',
        "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
        "create task": 'POST /api/v1/accounts/<username>/tasks',
        "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
        "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
        "delete task": 'DELETE /api/v1/accounts/<username>/tasks/<id>'
    }
    return jsonify(output)

@app.route('/api/v1/accounts/<username>/tasks', methods=['POST'])
def create_task(username):
    """Create a task for one user."""
    user = User.query.filter_by(username=username).first()
    
    if user:
        
        task = Task(
            name=request.form['name'],
            note=request.form['note'],
            creation_date=datetime.now(),
            due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
            completed=bool(request.form['completed']),
            user_id=user.id,
        )
        
        db.session.add(task)
        db.session.commit()
        
        output = {'msg': 'posted'}
        response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
        )
        return response

