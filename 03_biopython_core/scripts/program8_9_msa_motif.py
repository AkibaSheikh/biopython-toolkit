import re
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Program 8: store three sequences that are already aligned (same length)
sequences = [
    SeqRecord(Seq("ATGCTGACTAGCTAGCTAGC"), id="Seq1"),
    SeqRecord(Seq("ATGCTGACTAGCTAGCTGGC"), id="Seq2"),
    SeqRecord(Seq("ATGCTGACTAGCTAGCTTGC"), id="Seq3"),
]
alignment = MultipleSeqAlignment(sequences)
AlignIO.write(alignment, "alignment.fasta", "fasta")
print(alignment)

# Program 9: motif search (positions are 0-based)
sequence = Seq("ATGCTGACTAGCTAGCTAGC")
motif = "CTG"
matches = [m.start() for m in re.finditer(motif, str(sequence))]
print("Motif Matches:", ", ".join(map(str, matches)))