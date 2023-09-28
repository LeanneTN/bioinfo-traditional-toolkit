from web.controller import sca_blueprint
from web.service.SCAService import get_gc_content, get_gc_content_numpy, reverse_seq, complementary_dna
import json


@sca_blueprint.route('/', methods=["GET"])
def SCACheck():
    return {
        'module': 'Sequence Composition Analysis',
        'status': 'OK'
    }


@sca_blueprint.route('/gc_content/<seq>', methods=["GET"])
def get_gc_content_controller(seq):
    return {'gc content': get_gc_content(seq)}


@sca_blueprint.route('/gc_content_numpy/<seq>', methods=["GET"])
def get_gc_content_numpy_controller(seq):
    return {'gc content': get_gc_content_numpy(seq)}


@sca_blueprint.route('/reverse_seq/<seq>', methods=["GET"])
def reverse_seq_controller(seq):
    return {'reverse sequence': reverse_seq(seq)}


@sca_blueprint.route('/complementary_dna/<seq>', methods=["GET"])
def complementary_dna_controller(seq):
    return {'complementary DNA sequence': complementary_dna(seq)}

