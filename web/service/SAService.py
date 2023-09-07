import json
from utils.sequence_alignment.Hamming import Hamming


def hamming_distance(seq1, seq2):
    hamming = Hamming(seq1, seq2)
    return hamming.Hamming_distance()
