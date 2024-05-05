from flask import Flask, jsonify
from tasks import long_task, short_task, retrieve_task, retrieve_all_tasks, update_task_name, delete_task_by_id
from database import initialize_database

app = Flask(__name__)

initialize_database()  # Initialize SQLite database

@app.route('/api/long-task')
def trigger_long_task():
    long_task.delay()
    return jsonify({'message': 'Long task triggered successfully'})

@app.route('/api/short-task')
def trigger_short_task():
    short_task.delay()
    return jsonify({'message': 'Short task triggered successfully'})

@app.route('/api/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    result = retrieve_task.delay(task_id).get()
    return jsonify({'task': result})

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    result = retrieve_all_tasks.delay().get()
    return jsonify({'tasks': result})

@app.route('/api/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    new_name = data.get('name')
    result = update_task_name.delay(task_id, new_name).get()
    return jsonify({'message': result})

@app.route('/api/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = delete_task_by_id.delay(task_id).get()
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')