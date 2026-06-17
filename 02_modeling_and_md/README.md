# 02 — Modeling & MD

## Purpose
Assess and characterize the effects of mutations on the protein structure and dynamics of MgrB, PhoP, PhoQ, and PmrB using 3D structural modeling and molecular dynamics simulations.

## Input
- **Protein sequences**: FASTA files containing the amino acid sequences of MgrB, PhoP, PhoQ, and PmrB from both the WT reference and the 5D3D mutant strain.
- **3D structures**: PDB files predicted by AlphaFold 3 for the WT and 5D3D variants, serving as the starting coordinates for the molecular dynamics simulations.

## Strain Selection (5D3D and WT)
Among the five polymyxin B-resistant isolates (MIC > 64 µg/mL), strain 5D3D was selected for structural modeling and MD analyses based on:
- Highest mutational load across the regulatory cascade (substitutions and deletions in mgrB, phoP, phoQ, and pmrB)
- Extensive amino acid deletions in PmrB C-terminus and PhoP N-terminus
- Mutations classified by PROVEAN as deleterious in both phoP and pmrB
- Wild-type pmrA sequence across the entire coding region (internal structural reference)

For all structural evaluations, the wild-type (WT) structure of each protein was modeled and used as a baseline reference to compare against the mutant variants from the 5D3D strain.

## 3D Modeling
- **AlphaFold 3** — structural prediction for MgrB, PhoP, PhoQ, PmrB (WT + 5D3D variants) and PmrA (WT-only), totaling 9 models
- **Model selection** — highest pLDDT (> 90) and lowest PAE (< 5 Å)
- **Validation** — ProSA (Z-score), PROCHECK (Ramachandran), QMEANDisCo (global quality)
- **Pre-processing** — removal of steric contacts prior to simulation

## Molecular Dynamics Simulations
- **Engine** — GROMACS 2023.4 with GROMOS 53A6 force field
- **Setup** — SPC water, 0.15 M NaCl, periodic boundary conditions
- **Equilibration** — steepest descent (50,000 steps) → NVT (300 K) → NPT (300 K, 1 atm)
- **Production** — 100 ns NPT, 2 fs time step, LINCS constraints
- **Analyses** — RMSD, RMSF, Rg, SASA, H-bonds, electrostatic surface potential (APBS–PDB2PQR)

## Structure
```
02_modeling_and_md/
├── md_outputs/           # XVG files from GROMACS analyses (RMSD, RMSF, Rg, SASA, H-bonds)
├── md_setup_files/       # MDP files used for GROMACS simulations
└── models/               # Models in PDB format
```
