from flask import Blueprint


ex = Blueprint('example',__name__)

@ex.route('/')
def index():
    return "Bismillah"