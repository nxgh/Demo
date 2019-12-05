from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

from . import hello