import base64
import binascii
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

DEFAULT_ENTROPY = 32


# Functions above will be removed after python 3.6 will be provided in default
# ubuntu installation

def token_bytes(nbytes=None):
    if nbytes is None:
        nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)


def token_hex(nbytes=None):
    return binascii.hexlify(token_bytes(nbytes)).decode('ascii')


def token_urlsafe(nbytes=None):
    tok = token_bytes(nbytes)
    return base64.urlsafe_b64encode(tok).rstrip(b'=').decode('ascii')


def change_secret_key():
    """Change ``SECRET_KEY``"""
    secret_key = token_urlsafe(50)

    file_path = os.path.join(PROJECT_DIRECTORY, 'src/config/settings/local.py')

    with open(file_path) as f:
        file_content = f.read()

    file_content = file_content.replace('CHANGEME!', secret_key, 1)

    with open(file_path, 'w') as f:
        f.write(file_content)


change_secret_key()
