SDB (Simple Django Boilerplate)
===============================

A minimal cookiecutter template to generate a very simple django 1.10 project.

To generate new django project:

.. code::

    cookiecutter https://github.com/singleton11/SDB

Project will have the following directory structure:

.. code::

    <project_slug>
    ├── apps
    │   └── __init__.py
    ├── <project_slug>
    │   ├── __init__.py
    │   ├── settings
    │   │   ├── common.py
    │   │   ├── __init__.py
    │   │   ├── local.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── docker-compose.yml
    ├── tasks.py
    ├── manage.py
    ├── README.rst
    └── requirements
        ├── common.in
        └── local.in


Philosophy of the project is stay simple and easy to maintain

Now this boilerplate hasn't many useful things, but it will be added with trying to avoid to loose simplicity.

Changelog
#########

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