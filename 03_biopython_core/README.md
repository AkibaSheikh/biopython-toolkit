# 03_biopython_core

- **Goal:** Use Biopython for sequences, GC content, translation, alignment and BLAST.
- **Data:** sequence.fasta ([what it contains, for example gene name and length]).
- **What I did:** Read and wrote FASTA files, computed GC content and molecular weight, reverse-complemented and translated DNA, ran pairwise and multiple alignments, searched a motif, and ran BLAST from Python.
- **Result:** [for example: GC content 50.0%; BLAST top hit organism: ...].
- **Files:** scripts/ (Programs 1 to 10), plus the small FASTA files they read and write.
- **How to run:** source ~/bioinfo/venv/bin/activate, then cd 03_biopython_core and python scripts/program1_seqio.py