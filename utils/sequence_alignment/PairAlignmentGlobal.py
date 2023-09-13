import numpy as np
import pandas as pd


class PairAlignmentGlobal:
    """Class for global alignment of two sequences"""

    def __init__(self, seq1, seq2, match_score=1, mismatch_score=-1, gap_score=-1):
        """Initialize the class with two sequences and the scoring scheme"""
        self.seq1 = seq1
        self.seq2 = seq2
        self.match_score = match_score
        self.mismatch_score = mismatch_score
        self.gap_score = gap_score  # gap is indel in the sequence
        self.aligned_seq1 = ""
        self.aligned_seq2 = ""
        self.score = 0

    def score_matrix(self):
        """Calculate the score matrix for the alignment"""
        len1 = len(self.seq1)
        len2 = len(self.seq2)
        dp = np.zeros((len1 + 1, len2 + 1))
        for i in range(len1 + 1):
            dp[i][0] = i * self.gap_score
        for j in range(len2 + 1):
            dp[0][j] = j * self.gap_score

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                delta = self.match_score if self.seq1[i - 1] == self.seq2[j - 1] else self.mismatch_score
                dp[i][j] = max(dp[i - 1][j - 1] + delta,
                               max(dp[i - 1][j] + self.gap_score, dp[i][j - 1] + self.gap_score))
        self.score = dp[len1][len2]
        return dp

    def Needleman_Wunsch(self):
        pass

    def Smith_Waterman(self):
        """
        Calculate the score matrix for the alignment. Attention, Smith-Waterman algorithm is a local alignment,
        but it is the variation of Needleman-Wunsch algorithm. Thus, I put it into this class.
        :return: score matrix and the best-matched sequence
        """
        len1 = len(self.seq1)
        len2 = len(self.seq2)
        dp = np.zeros((len1 + 1, len2 + 1))
        for i in range(len1 + 1):
            dp[i][0] = 0
        for j in range(len2 + 1):
            dp[0][j] = 0

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                delta = self.match_score if self.seq1[i - 1] == self.seq2[j - 1] else self.mismatch_score
                dp[i][j] = max(dp[i - 1][j - 1] + delta,
                               max(dp[i - 1][j] + self.gap_score, dp[i][j - 1] + self.gap_score, 0))
        self.score = dp[len1][len2]
        pos = np.unravel_index(np.argmax(dp, axis=None), dp.shape)
        match_seq = ""
        seq1_list = list(self.seq1)
        seq1_list.insert(0, '-')
        seq2_list = list(self.seq2)
        seq2_list.insert(0, '-')
        matrix_score = pd.DataFrame(dp, columns=seq2_list, index=seq1_list)
        i, j = pos
        while i > 0 and j > 0:
            if dp[i][j] > 0:
                match_seq = matrix_score.columns[j] + match_seq
                if dp[i - 1][j - 1] > 0:
                    i -= 1
                    j -= 1
                else:
                    break
            else:
                break
        return matrix_score, match_seq
