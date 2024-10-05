// static/script.js

// Fetch all tasks and display them
function fetchTasks() {
    fetch('/get_tasks')
        .then(response => response.json())
        .then(tasks => {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = ''; // Clear existing tasks
            tasks.forEach(task => {
                const taskItem = document.createElement('li');
                taskItem.innerText = task[1];
                const deleteBtn = document.createElement('button');
                deleteBtn.innerText = 'Delete';
                deleteBtn.onclick = () => deleteTask(task[0]);
                taskItem.appendChild(deleteBtn);
                taskList.appendChild(taskItem);
            });
        });
}

// Add a new task
function addTask() {
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value;
    fetch('/add_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task })
    })
    .then(response => response.json())
    .then(() => {
        taskInput.value = '';
        fetchTasks();
    });
}

// Delete a task by ID
function deleteTask(id) {
    fetch('/delete_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id })
    })
    .then(response => response.json())
    .then(() => fetchTasks());
}

// Load tasks on page load
document.addEventListener('DOMContentLoaded', fetchTasks);
