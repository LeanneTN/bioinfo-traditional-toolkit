import numpy as np


class SimilarityScore:
    def __init__(self, *seqs):
        self.seqs = seqs

    def length_check(self):
        """
        Check if all sequences have the same length
        :return: boolean
        """
        length = len(self.seqs[0])
        for seq in self.seqs:
            if len(seq) != length:
                return False
        return True

    def pair_distance(self, score='edit'):
        """
        Calculate the edit distance between two sequences
        :return: int edit distance
        """
        len1 = len(self.seqs[0])
        len2 = len(self.seqs[1])
        dp = np.zeros((len1 + 1, len2 + 1))
        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        reward = 1
        penalty = 0
        if score == 'edit':
            pass
        elif score == 'BLAST':
            reward = 5
            penalty = -4

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                delta = reward if self.seqs[0][i - 1] == self.seqs[1][j - 1] else penalty
                dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1))
        return dp[len1][len2]

