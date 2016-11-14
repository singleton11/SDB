from fabric.api import local


def startapp():
    """Create app from cookiecutter template"""
    local('cookiecutter https://github.com/singleton11/sdjat -o '
          '{{cookiecutter.project_slug}}/apps')
