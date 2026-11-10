from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction, molecular_weight

sequence = Seq("ATGCTGACTAGCTAGCTAGC")

# Program 2: GC content (gc_fraction gives 0 to 1, so multiply by 100)
gc_content = gc_fraction(sequence) * 100
print(f"GC content: {gc_content}%")

# Program 4: molecular weight
weight = molecular_weight(sequence)
print("Molecular Weight:", weight)