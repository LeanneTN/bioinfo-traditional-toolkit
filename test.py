import utils.sequence_alignment.Hamming as Hamming
import utils.sequence_alignment.SimilarityScore as SimilarityScore

if __name__ == '__main__':
    seq1 = "ATGTTAT"
    seq2 = "ATCGTAC"
    similarity = SimilarityScore.SimilarityScore(seq1, seq2)
    print(similarity.pair_distance())