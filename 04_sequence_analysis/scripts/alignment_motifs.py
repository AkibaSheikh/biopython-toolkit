from Bio import Align

aligner = Align.PairwiseAligner()
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -5
aligner.extend_gap_score = -0.5

for mode in ("global", "local"):
    aligner.mode = mode
    result = aligner.align("ATCGAGCTAGC", "ATGGGCTAGC")
    print(mode, "score =", result.score)
    print(result[0])
    