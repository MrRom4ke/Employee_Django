# Employee directory (django)
Web-application which displays a tree structure of departments with a list of employees

## About

Information about each employee is stored in a database and
contains the following data: <br>
FULL NAME; <br>
Job title; <br>
Employment date; <br>
The amount of wages; <br>
Division - divisions have a structure of up to 5 levels.
 
Initially, the tree is displayed collapsed.
 
The database is filled with a script `db_seeder.py`
 
CRUD records are managed through the Django admin

## Tech Stack

The project is currently running on the following versions:

Backend:
* Python 3.10
* Django 4.1.2
* django-mptt 0.14.0

Frontend:
* Bootstrap 5.2.2
* Jquery

Test values for the database:
* django-seed 0.3.1
* Faker 15.1.1

## Running Locally

To run the project locally first you need to clone the repository:
```
git clone https://github.com/MrRom4ke/Employee_Django.git
```
Create a virtualenv:
```
virtualenv venv -p python3
```
Install the development requirements:
```
pip install -r requirements/local.txt
```
Populate the database with test values, it takes about 9 minutes:
```
python3 manage.py runscript db_seeder
```
Run the local server:
```
python3 manage.py runserver
```
## License
The source code is released under the [MIT License](https://github.com/vitorfs/parsifal/blob/master/LICENSE).
## Author
MrRom4ke