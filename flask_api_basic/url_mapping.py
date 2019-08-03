
import example

def url_mappings(app):
    app.register_blueprint(example.ex)
    return app