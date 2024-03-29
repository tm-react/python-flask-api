## How to start Pythong Flask Project?

1. Check you have installed Python 3, Download Link https://www.python.org/downloads/
2. Run Below commands for Application setup

```bash
mkdir flask_api
cd flask_api

virtualenv venv  # For create Application Specific Environment
```

3. if you are using git VCS then can setup .gitignore

```
__pycache__/
*.py[cod]
*$py.class

venv
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
```

4. Create a setup.py file for setuptools. https://pypi.org/project/setuptools/

```python
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
```

**For Install the App Run Command**:  python setup.py install

**For development the App Run Command**: python setup.py develop

5. Create a app_config.py for store application configuration, such as **port**, **host** etc

```python
# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production
```

6. Create a example.py for example route.

```python
from flask import Blueprint


ex = Blueprint('example',__name__)

@ex.route('/')
def index():
    return "Bismillah"
```

8. Create a url_mapping.py for add all route.

```python
import example

def url_mappings(app):
    app.register_blueprint(example.ex)
    return app
```


9.  Create a application.py for application startup.

```python
from flask import Flask
import app_config
import url_mapping


app = Flask(__name__)


def flask_configuration(flask_app):
    flask_app.config['SERVER_NAME'] = app_config.FLASK_SERVER_NAME


def init_configurations(flask_app):
    flask_configuration(flask_app)



def bismillah():
    init_configurations(app)   
    url_mapping.url_mappings(app)
    app.run(debug=app_config.FLASK_DEBUG)




if __name__ == "__main__":
    bismillah()
```