from flask import Blueprint
from web.controller.SAController import hamming_distance_controller

blueprint = Blueprint('SA', __name__, url_prefix='/SA')

blueprint.route('/hamming_distance', methods=['GET'])(hamming_distance_controller)