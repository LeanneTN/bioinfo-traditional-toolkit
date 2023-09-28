import utils.sequence_alignment.Hamming as Hamming
import utils.sequence_alignment.SimilarityScore as SimilarityScore
from utils.static_data.SA.DNA.SubstitutionMatrix import SubstitutionMatrix as DNASubstitutionMatrix
from utils.sequence_alignment.PairAlignmentGlobal import PairAlignmentGlobal
from utils.sequence_character_analysis.DNASequenceCharacterAnalysis import DNASequenceCharacterAnalysis

if __name__ == '__main__':
    pair_alignment = PairAlignmentGlobal('ATACCGCG', 'ACCG', 1, -1, -2)
    print(pair_alignment.Smith_Waterman()[0])

    dna = DNASequenceCharacterAnalysis('ATACCGCG')
    print(dna.get_gc_content_numpy())