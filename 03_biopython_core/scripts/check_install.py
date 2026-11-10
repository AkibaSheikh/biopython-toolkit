from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

dna = Seq("ATGCTGACTAGCTAGCTAGC")
print("Length:", len(dna))
print("GC %:", round(gc_fraction(dna) * 100, 1))
print("Reverse complement:", dna.reverse_complement())
print("RNA:", dna.transcribe())
print("Protein:", dna[:18].translate())