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