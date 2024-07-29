#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    
    users_response = requests.get(f"{url}/users")
    users = users_response.json()
    
    all_tasks = {}
    
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks_response = requests.get(f"{url}/todos?userId={user_id}")
        tasks = tasks_response.json()
        
        all_tasks[user_id] = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in tasks
        ]
    
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)

