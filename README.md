Project written in Python 3 & Django 3.1.5 

# install pyenv
https://github.com/pyenv/pyenv-installer

# Install a virtualenv wrapper
https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html

# PostGreSQL
First of all create a new Postgres database for this project: 
` CREATE DATABASE ten_db;`

## Insert data via command line 

`Note: duplicate rows from CSVs have been removed`
insert inventory:
```
python manage.py runscript upload_file --script-args Inventory.csv
```

insert inventory:
```
python manage.py runscript upload_file --script-args Members.csv
```

## Unit Testing
Run tests: `pytest`