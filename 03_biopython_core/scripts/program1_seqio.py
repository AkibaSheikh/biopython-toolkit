from Bio import SeqIO

# Read sequences from a FASTA file
for sequence in SeqIO.parse("sequence.fasta", "fasta"):
    print("ID:", sequence.id)
    print("Length:", len(sequence))

# Write the records back out to a new file
records = list(SeqIO.parse("sequence.fasta", "fasta"))
count = SeqIO.write(records, "output.fasta", "fasta")
print("Records written:", count)