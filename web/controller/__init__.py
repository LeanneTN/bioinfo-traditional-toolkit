from flask import Blueprint

sa_blueprint = Blueprint('sa', __name__, url_prefix='/sa')
sca_blueprint = Blueprint('sca', __name__, url_prefix='/sca')

