# Welcome
This project contains apis which can perform CRUD operations on a database and return a response in json format.
# Usage
1. Creating a virtual environment is advised. Execute the following command:
```
pip3 -m venv [name_of_dir]
```
2. Then install the dependencies from requirements.txt file. This can be done by executing the following command:
```
pip3 install -r requirements.txt
```
3. Using fastapi run app.py:
```
fastapi dev app.py
```
4. Now, either go to the url provided in the terminal and access the api from there or go to postman instead.
# Files
## app.py
This is python script which contains our apis for get, post, put, patch, delete methods.
## constants.py
This is a python script which contains our constant values like data, queries and strings which will be returned.
## methods.py
This is a python script which contains methods which will connect with the database and execute queries.
## requirements.txt
This is a txt file containing the requirements of our project.
This is to be used with pip to automatically install dependencies.