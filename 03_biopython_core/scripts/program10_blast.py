import io
import re
from Bio.Blast import NCBIWWW, NCBIXML

program = "blastp"            # protein query vs protein database
database = "nr"               # NCBI non-redundant protein database
query_sequence = "JAO23553.1" # accession of the query protein

print("Running BLAST, please wait...")
result_handle = NCBIWWW.qblast(program, database, query_sequence)

# Read the XML once, then close the handle
blast_xml = result_handle.read()
result_handle.close()

# Save the raw result
with open("blast_results.xml", "w") as out_handle:
    out_handle.write(blast_xml)

# Parse the same text (not the empty handle)
blast_record = NCBIXML.read(io.StringIO(blast_xml))

# Organism is in square brackets in the top hit's title
top_hit_description = blast_record.alignments[0].title
organism_match = re.search(r"\[.*?\]", top_hit_description)
organism = organism_match.group(0).strip("[]") if organism_match else "Organism information not available"
print("Organism:", organism)