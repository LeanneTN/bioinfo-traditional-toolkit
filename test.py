import utils.sequence_alignment.Hamming as Hamming
import utils.sequence_alignment.SimilarityScore as SimilarityScore
from utils.static_data.SA.DNA.SubstitutionMatrix import SubstitutionMatrix as DNASubstitutionMatrix
from utils.sequence_alignment.PairAlignmentGlobal import PairAlignmentGlobal

if __name__ == '__main__':
    pair_alignment = PairAlignmentGlobal('ATACCGCG', 'ACCG', 1, -1, -2)
    print(pair_alignment.Smith_Waterman()[0])