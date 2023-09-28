import copy

import numpy as np


class DNASequenceCharacterAnalysis:
    def __init__(self, seq):
        self.seq = seq

    def get_gc_content(self):
        """
        Get the GC content of a DNA sequence
        :return: float GC content
        """
        gc = 0
        for char in self.seq:
            if char == 'G' or char == 'C':
                gc += 1
        return gc / len(self.seq)

    def get_gc_content_numpy(self):
        """
        Get the GC content of a DNA sequence using numpy, faster than get_gc_content in the long sequence
        :return: float GC content
        """
        l = len(self.seq)
        seq = np.array(self.seq)
        num_g = np.char.count(seq, 'G')
        num_c = np.char.count(seq, 'C')
        return (num_g + num_c) / l

    def reverse_seq(self):
        """
        Reverse a sequence
        :param seq: str
        :return: str
        """
        return self.seq[::-1]

    def complementary_dna(self):
        """
        Get the complementary DNA sequence of a DNA sequence
        :param seq: the original DNA sequence
        :return: Complementary DNA sequence
        """
        dna_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complementary_dna_seq = copy.deepcopy(self.seq)
        seq_list = list(complementary_dna_seq)
        for i in range(len(self.seq)):
            seq_list[i] = dna_dict[self.seq[i]]
        complementary_dna_seq = ''.join(seq_list)
        return complementary_dna_seq
