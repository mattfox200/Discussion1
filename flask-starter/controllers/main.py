from flask import *
from extensions import mysql

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/hello')
def hello():
    return "Hello everyone!"