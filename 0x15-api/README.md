## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python

## Tasks
### 0. Gather data from an API
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
	* File: [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py)
### 1. Export to CSV
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:
* Records all tasks that are owned by this employee
* Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
* Output File name must be: USER_ID.csv
	* File: [1-export_to_CSV.py](1-export_to_CSV.py)
### 2. Export to JSON
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:
* Records all tasks that are owned by this employee
* Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
* Output File name must be: USER_ID.json
	* File: [2-export_to_JSON.py](2-export_to_JSON.py)
### 3. Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:
* Records all tasks from all employees
* Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
* Output File name must be: todo_all_employees.json
	* File: [3-dictionary_of_list_of_dictionaries.py](3-dictionary_of_list_of_dictionaries.py)
