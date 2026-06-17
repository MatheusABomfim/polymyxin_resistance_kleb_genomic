# 05 — Alignments

## Purpose
Compare the nucleotide and amino acid sequences of the pmrA, pmrB, phoP, phoQ, and mgrB loci across the polymyxin-resistant isolates to locate the mutations analyzed in the other modules and assess their conservation against a reference.

## Input
- Gene sequences of pmrA, pmrB, phoP, phoQ, mgrB from strains 2D2A, 2D4A.1, 2D4A.2, 2D4B, 5D3D
- Protein sequences from `../02_modeling_and_md/models/protein_sequences/` (MGRB, PHOP, PHOQ, PMRA, PMRB)
- A reference sequence (REF) for each locus

## Tools
- **MEGA** — multiple sequence alignment of nucleotide and protein sequences
- **Jalview** — alignment visualization, consensus, and ClustalX residue coloring

## Output
Each locus has a gene-level and a protein-level alignment figure:

```
05_alignments/
├── MGRB_genes.png      # mgrB nucleotide alignment
├── MGRB_proteins.png   # MgrB protein alignment
├── PHOP_genes.png      # phoP nucleotide alignment
├── PHOP_proteins.png   # PhoP protein alignment
├── PHOQ_genes.png      # phoQ nucleotide alignment
├── PHOQ_proteins.png   # PhoQ protein alignment
├── PMRA_genes.png      # pmrA nucleotide alignment
├── PMRA_proteins.png   # PmrA protein alignment
├── PMRB_genes.png      # pmrB nucleotide alignment
└── PMRB_proteins.png   # PmrB protein alignment
```

Each figure shows the aligned sequences for REF and the five strains, the consensus logo, and the consensus sequence.
