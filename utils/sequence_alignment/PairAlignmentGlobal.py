
class PairAlignmentGlobal:
    """Class for global alignment of two sequences"""

    def __init__(self, seq1, seq2, match_score=1, mismatch_score=-1, gap_score=-1):
        """Initialize the class with two sequences and the scoring scheme"""
        self.seq1 = seq1
        self.seq2 = seq2
        self.match_score = match_score
        self.mismatch_score = mismatch_score
        self.gap_score = gap_score
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
                dp[i][j] = max(dp[i - 1][j - 1] + delta, max(dp[i - 1][j] + self.gap_score, dp[i][j - 1] + self.gap_score))
        self.score = dp[len1][len2]
        return dp
