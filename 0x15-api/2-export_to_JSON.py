#!/usr/bin/python3
"""
This script fetches data from a REST API and exports an employee's TODO list progress to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)
    
    # Fetch employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list data
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    if not user_data:
        print(f"No employee with ID {employee_id} found.")
        sys.exit(1)

    employee_name = user_data.get('username')
    user_id = user_data.get('id')

    # Prepare data for JSON export
    tasks = []
    for task in todos_data:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        }
        tasks.append(task_dict)
    
    json_data = {str(user_id): tasks}

    # Define JSON file name
    json_filename = f"{user_id}.json"

    # Write to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {json_filename}")

