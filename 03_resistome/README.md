# 03 — Resistome

## Purpose
Investigate the presence of antimicrobial resistance-associated determinants in the analyzed isolates through homology-based screening of the pmrA, pmrB, phoP, phoQ, and mgrB loci against multiple curated resistance databases.

## Input
- `data/polinny.fa` — Combined FASTA with pmrAB, phoPQ, mgrB sequences from strains 2D2A, 2D4A.1, 2D4A.2, 2D4B, 5D3D

## Tool
- **ABRIcate** (https://github.com/tseemann/abricate) — homology-based resistome annotation

## Databases
- **CARD** (doi:10.1093/nar/gkac920)
- **ResFinder** (doi:10.1093/jac/dkaa345)
- **NCBI AMRFinderPlus** (doi:10.1038/s41598-021-91456-0)
- **ARG-ANNOT** (doi:10.1128/AAC.01310-13)
- **MEGARes** (doi:10.1093/nar/gkac1047)
- **VFDB** (virulence factors) (pubmed:15608208)
- **PlasmidFinder** (plasmid replicons) (doi:10.1128/AAC.02412-14)

## Output
- `abricate_results/*.txt` — Per-database screening results
- `abricate_results/abricate_polinny.tsv` — Merged summary
- `abricate_results/abricate_polinny_multi.tsv` — Multi-hit summary

## Key Findings
- Hits detected **only in MEGARes**: PHOR (SMR efflux regulator, ≈100% coverage, ≈99.6–99.8% identity) and CTX (class A β-lactamase, ≈100% coverage, ≈97.3–97.4% identity)
- No acquired AMR genes in CARD, ResFinder, NCBI, ARG-ANNOT
- No virulence factors (VFDB) or plasmid replicons (PlasmidFinder)

## Environment Setup
See `requirements.txt` for installation instructions.

## Commands
```bash
for db in card resfinder ncbi argannot megares vfdb plasmidfinder; do
    abricate --db $db data/polinny.fa > abricate_results/${db}.txt
done
abricate --summary abricate_results/*.txt > abricate_results/abricate_polinny.tsv
```
