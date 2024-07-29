#!/usr/bin/python3
"""
This script fetches data from a REST API and exports an employee's TODO list progress to a CSV file.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    # Define CSV file name
    csv_filename = f"{user_id}.csv"

    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([user_id, employee_name, task.get('completed'), task.get('title')])

    print(f"Data exported to {csv_filename}")

