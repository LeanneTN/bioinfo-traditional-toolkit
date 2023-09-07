class Hamming:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def length_check(self):
        if len(self.seq1) == len(self.seq2):
            return True
        return False

    def Hamming_distance(self):
        if self.length_check():
            distance = 0
            for char1, char2 in zip(self.seq1, self.seq2):
                if char1 != char2:
                    distance += 1
            return distance
        else:
            return "length is different"

