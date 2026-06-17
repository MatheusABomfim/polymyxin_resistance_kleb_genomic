# 01 — PROVEAN

## Purpose
Predict whether amino acid substitutions identified in pmrAB, phoPQ, and mgrB have a deleterious effect on protein function using the PROVEAN (Protein Variation Effect Analyzer) tool.

## Input
- `data/` — Amino acid sequences and mutation lists for each gene

## Output
- `results/` — PROVEAN scores and classification (deleterious / neutral) per substitution

## Structure
```
01_provean/
├── data/          # Input sequences and mutation lists
├── scripts/       # Batch submission and parsing scripts
└── results/       # PROVEAN predictions and summaries
```
