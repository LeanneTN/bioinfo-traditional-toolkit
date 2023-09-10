import pandas as pd
import numpy as np


class SubstitutionMatrix:
    def __init__(self):
        unitary_matrix = [[None, 'A', 'T', 'C', 'G'],
                          ['A', 1, 0, 0, 0],
                          ['T', 0, 1, 0, 0],
                          ['C', 0, 0, 1, 0],
                          ['G', 0, 0, 0, 1]]
        self.unitary_matrix = pd.DataFrame(unitary_matrix)
        transition_transversion = [[None, 'A', 'T', 'C', 'G'],
                                   ['A', 1, -5, -5, -1],
                                   ['T', -5, 1, -1, -5],
                                   ['C', -5, -1, 1, -5],
                                   ['G', -1, -5, -5, 1]]
        self.transition_transversion = pd.DataFrame(transition_transversion)
        blast = [[None, 'A', 'T', 'C', 'G'],
                 ['A', 5, -4, -4, -4],
                 ['T', -4, 5, -4, -4],
                 ['C', -4, -4, 5, -4],
                 ['G', -4, -4, -4, 5]]
        self.blast = pd.DataFrame(blast)

    def get_unitary_matrix(self):
        return self.unitary_matrix