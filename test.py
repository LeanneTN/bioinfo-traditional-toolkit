import utils.sequence_alignment.Hamming as Hamming

if __name__ == '__main__':
    seq1 = "GGGCCGTTGGT"
    seq2 = "GGACCGTTGAC"
    hamming = Hamming.Hamming(seq1, seq2)
    print(hamming.Hamming_distance())