import json
from utils.sequence_alignment.Hamming import Hamming
from utils.sequence_alignment.PairAlignmentGlobal import PairAlignmentGlobal


def hamming_distance(seq1, seq2):
    hamming = Hamming(seq1, seq2)
    return hamming.Hamming_distance()

def Smith_Waterman(seq1, seq2):
    pair_alignment = PairAlignmentGlobal(seq1, seq2)
    return pair_alignment.Smith_Waterman()
