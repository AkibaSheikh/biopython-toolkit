from Bio import Align

seq1 = "ATCGAGCTAGC"
seq2 = "ATGGGCTAGC"

aligner = Align.PairwiseAligner()
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -5
aligner.extend_gap_score = -0.5

# Global alignment: compares the sequences across their whole length
aligner.mode = "global"
alignments = aligner.align(seq1, seq2)
print("GLOBAL score:", alignments.score)
for alignment in alignments:
    print(alignment)

# Local alignment: finds the best matching region only
aligner.mode = "local"
alignments = aligner.align(seq1, seq2)
print("LOCAL score:", alignments.score)
print(alignments[0])