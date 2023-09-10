import utils.sequence_alignment.Hamming as Hamming
import utils.sequence_alignment.SimilarityScore as SimilarityScore
from utils.static_data.SA.DNA.SubstitutionMatrix import SubstitutionMatrix as DNASubstitutionMatrix

if __name__ == '__main__':
    substitute_matrix = DNASubstitutionMatrix()
    print(substitute_matrix.get_unitary_matrix())