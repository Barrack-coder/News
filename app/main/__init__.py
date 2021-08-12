from flask import Blueprint
from flask import flask 
main = Blueprint('main',__name__)
from . import views,error
