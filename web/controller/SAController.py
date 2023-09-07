from web.service.SAService import hamming_distance
import json


def check():
    return {
        'status': 'OK'
    }


def hamming_distance_controller():
    return hamming_distance()
