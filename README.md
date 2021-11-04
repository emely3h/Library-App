# Flask Library App

This is a very basic library app as assesment project for the SE_01 module.

So far the basic features are:

* A user can register and login (with proper form validators and error messages).
* A user can logout.
* A user can add books to the bookshelf.
* The bookshelf provides an alphabetical overview of all books.
* Detail view for every book.
* A user can add a book to the reading list.
* A user can rent a book.
* In the profile page every user has an overview of the reading books and the currently rented books with their duedate.
* A user can remove books from the reading list.
* A user can give back rented books.

However the app is not even close to being finised. Some next steps would be:

  Books in reading list should be unique
  Only an admin should be allowed to add books to the bookshelf.
  Error handling for db errors
  Deploy to Heruku
  Handle multiple similar books.
  Admin overview of currently rented books + due date + possibility to edit a book.



## Local Setup

### Virtual Environment

To install this locally, clone the repository. 

Then, you need to first create and activate a virtual environment: 

* `python3 -m venv venv`
* `source venv/bin/activate`

Now, you need to install all the packages in the requirements.txt file by running: 

`pip install -r requirements.txt`

### Environemnt Variables

Secondly, you need to set up your .env file. By default that file should be ignored and not committed to GitHub. Check out the file **.env.example**. This is an example for what the **.env** file looks like. Make sure to create that file with a similar set up before you start your server locally.

### Database Setup

Lastly, your database needs to be set up. Locally, the database is stored in a database.db SQLite file. We also don't commit that to GitHub because it's dynamic data that changes around whenever we add new records. So you need to set that up locally before you get started as well. 

* So run: `flask db init` to initialize the database. 
* Then, run `flask db upgrade` to actually execute all the migrations stored in the **migrations** folder. That will generate the database tables. 

### Run the server

Now you can **startup the server by running**:

```
python run.py
```

## Making changes to the database

Whenever you make any changes to your models (e.g. add columns) you need to create a new migration. To do that run the following two commands: 

```
flask run migrate -m 'migration description'
flask db upgrade
```

Replace 'migration description' with your own description that describes what the migration added or removed. 
