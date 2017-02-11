SDB (Simple Django Boilerplate)
===============================

A minimal cookiecutter template to generate a very simple django 1.10 project.

To generate new django project:

.. code::

    cookiecutter https://github.com/singleton11/SDB

Project will have the following directory structure:

.. code::

    <project_slug>
    ├── docker-compose.yml
    ├── Pipfile
    ├── README.rst
    └── src
        ├── apps
        │   └── __init__.py
        ├── config
        │   ├── __init__.py
        │   ├── settings
        │   │   ├── common
        │   │   │   ├── base.py
        │   │   │   ├── __init__.py
        │   │   │   ├── installed_apps.py
        │   │   │   ├── localization.py
        │   │   │   ├── middleware.py
        │   │   │   ├── security.py
        │   │   │   ├── staticfiles.py
        │   │   │   └── templates.py
        │   │   ├── __init__.py
        │   │   └── local.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── core
        │   ├── apps.py
        │   └── __init__.py
        └── manage.py

Then to create virtualenv and install dependencies you have to run

.. code::

    pipenv install

To activate virtualenv

.. code::

    pipenv shell

Philosophy of the project is stay simple and easy to maintain

Now this boilerplate hasn't many useful things, but it will be added with trying to avoid to loose simplicity.

Changelog
#########

2017-02-11
**********

- Added core app
- Django app moved to ``src/``
- ``pip-tools`` replaced to ``pipenv``
- Split settings

2016-12-29
**********

- ``SECRET_KEY`` moved in ``local.py`` because ``SECRET_KEY`` have to set up through environment variables in production
  and purpose of this decision to make project be not able to start without environment variable with ``SECRET_KEY``
  value provided
- Added post-generation hook to change ``SECRET_KEY``

2016-12-28
**********

- Removed redundant dependencies from common.in and local.in
- Removed docker-compose web service (because, there is better development in virtual environment)
- Removed coverage settings (because pycharm has bundled coverage tool)
- Fabric replaced by invoke
- Adjusted README.rst title '#' symbol length by project name length
- Added PyCharm configuration

2016-11-28
**********

- Project restructuring
- Added ``pip-tools`` support
- Added a few fab commands

2016-11-12
**********

- Added README
- Added MIT LICENSE