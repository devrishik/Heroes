Heroes
======

A short description of the project.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Requirments
-----------

* Python 2.7
* VirtualEnv
* Postgres

Basic Commands
--------------

Setting Up Your Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 1st install and activate a virtualenv in your terminal

* Install dependencies

    $ pip install -r requirements/local.txt

* Update Database variables in Heroes/config/local.txt:50

Start the server
^^^^^^^^^^^^^^^^
To start the server

    $ python manage.py runserver 8000

Then open your browser and go to http://localhost:8000

Using the website
-----------------

The design and information flow of the app is a bit unconventional, it has been done to save time for this project

**Home Page**
    This is a List page for all the users in the database.
    This page is used on successful merging of two heroes or when a new hero is created. The new hero can be seen at the         bottom of the page. I could have created a Hero/<id> page but thats just extra code, and this project more time than i       thought it would take

**Merge Page**
    This page is used to merge to super heroes with their given `hero_name`

