SDB (Simple Django Boilerplate)
===============================

A minimal cookiecutter template to generate a very simple django 1.10 project.

To generate new django project:

.. code::

    cookiecutter https://github.com/singleton11/SDB

Project will have the following directory structure:

.. code::

    <project_slug>
    ├── docker
    │   └── web
    │       └── Dockerfile
    ├── docker-compose.yml
    ├── README.rst
    ├── requirements
    │   ├── base.txt
    │   └── local.txt
    └── <project_slug>
        ├── apps
        │   └── __init__.py
        ├── manage.py
        └── <project_slug>
            ├── __init__.py
            ├── settings
            │   ├── base.py
            │   ├── __init__.py
            │   └── local.py
            ├── urls.py
            └── wsgi.py

Philosophy of the project is stay simple and easy to maintain

Now this boilerplate hasn't many useful things, but it will be added with trying to avoid to loose simplicity.

Changelog
#########

2016-11-12
**********

- Added README
- Added MIT LICENSE