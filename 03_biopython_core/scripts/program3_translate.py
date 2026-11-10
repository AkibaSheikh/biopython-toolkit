from Bio.Seq import Seq

# Reverse complement
dna_small = Seq("GCG")
print("Reverse complement of GCG:", dna_small.reverse_complement())

# Transcription and translation
dna = Seq("ATGCTGACTAGCTAGCTAGC")
print("RNA:", dna.transcribe())

# Trim to a multiple of 3 to avoid the partial-codon warning
usable = len(dna) - (len(dna) % 3)
protein = dna[:usable].translate()
print("Protein:", protein)

# Same translation, stopping at the first stop codon
print("Protein (to_stop):", dna[:usable].translate(to_stop=True))