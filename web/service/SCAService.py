from utils.sequence_character_analysis.DNASequenceCharacterAnalysis import DNASequenceCharacterAnalysis


def get_gc_content(seq):
    """
    Get the GC content of a DNA sequence
    :return: float GC content
    """
    dna = DNASequenceCharacterAnalysis(seq)
    return dna.get_gc_content()


def get_gc_content_numpy(seq):
    """
    Get the GC content of a DNA sequence using numpy, faster than get_gc_content in the long sequence
    :return: float GC content
    """
    dna = DNASequenceCharacterAnalysis(seq)
    return dna.get_gc_content_numpy()


def reverse_seq(seq):
    """
    Reverse a sequence
    :param seq: str
    :return: str
    """
    return DNASequenceCharacterAnalysis(seq).reverse_seq()


def complementary_dna(seq):
    """
    Get the complementary DNA sequence of a DNA sequence
    :param seq: the original DNA sequence
    :return: Complementary DNA sequence
    """
    return DNASequenceCharacterAnalysis(seq).complementary_dna()
