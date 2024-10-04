# app.py

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    conn.close()
    return jsonify(tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.json['task']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Task added successfully!'})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_id = request.json['id']
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Task deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
