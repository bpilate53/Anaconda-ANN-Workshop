from flask import Flask, Blueprint, render_template, url_for, json, request, redirect
from todo.models import Task

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    all_tasks = Task().get_all()
    return render_template('todo/index.html', predictions = all_tasks)

@bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        new_task = Task().predict()
        return redirect(url_for('todo.index'))

    return render_template('todo/predict.html')
    