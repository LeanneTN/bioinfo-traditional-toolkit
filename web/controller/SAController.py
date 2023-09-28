from web.controller import sa_blueprint
from web.service.SAService import hamming_distance, Smith_Waterman
import json


@sa_blueprint.route('/', methods=["GET"])
def SACheck():
    return {
        'module': 'Sequence Alignment',
        'status': 'OK'
    }


@sa_blueprint.route('/hamming/<seq1>/<seq2>', methods=["GET"])
def hamming_distance_controller(seq1, seq2):
    return {'hamming distance' : hamming_distance(seq1, seq2)}

@sa_blueprint.route('/smith_waterman/<seq1>/<seq2>', methods=["GET"])
def smith_waterman_controller(seq1, seq2):
    result = Smith_Waterman(seq1, seq2)
    score_matrix = result[0]
    return {'score matrix': score_matrix,
            'best-matched sequence': result[1]}
