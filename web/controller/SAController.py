from web.controller import sa_blueprint
from web.service.SAService import hamming_distance
import json


@sa_blueprint.route('/check', methods=["GET"])
def check():
    return {
        'status': 'OK'
    }


@sa_blueprint.route('/hamming/<seq1>/<seq2>', methods=["GET"])
def hamming_distance_controller(seq1, seq2):
    return {'hamming distance' : hamming_distance(seq1, seq2)}
