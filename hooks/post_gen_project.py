import os
from secrets import token_urlsafe

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def change_secret_key():
    """Change ``SECRET_KEY``"""
    secret_key = token_urlsafe(50)

    file_path = os.path.join(PROJECT_DIRECTORY, 'config/settings/local.py')

    with open(file_path) as f:
        file_content = f.read()

    file_content = file_content.replace('CHANGEME!', secret_key, 1)

    with open(file_path, 'w') as f:
        f.write(file_content)
