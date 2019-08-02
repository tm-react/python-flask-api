from setuptools import setup, find_packages

setup(
    name='flask_api',
    version='1.0.0',
    description='Boilerplate code for a Python Flask RESTful API',
    url='https://github.com/tm-react/python-flask-api',
    author='H.M.Touhid Mia',

    packages=find_packages(),
    install_requires=[
        'Flask',
        'SQLAlchemy'
    ]
)
