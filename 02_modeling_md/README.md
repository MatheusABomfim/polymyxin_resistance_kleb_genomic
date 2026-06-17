# 02 — Modeling + MD

## Purpose
Identify and characterize mutations in pmrAB, phoPQ, and mgrB genes, perform 3D structural modeling, and conduct molecular dynamics simulations to evaluate the conformational consequences of the genetic alterations.

## Input
- `data/polinny.fa` — pmrAB, phoPQ, mgrB sequences from strains 2D2A, 2D4A.1, 2D4A.2, 2D4B, 5D3D

## Strain Selection (5D3D)
Among the five polymyxin B-resistant isolates (MIC > 64 µg/mL), strain 5D3D was selected for structural modeling and MD analyses based on:
- Highest mutational load across the regulatory cascade (substitutions and deletions in mgrB, phoP, phoQ, and pmrB)
- Extensive amino acid deletions in PmrB C-terminus and PhoP N-terminus
- Mutations classified by PROVEAN as deleterious in both phoP and pmrB
- Wild-type pmrA sequence across the entire coding region (internal structural reference)

## Three-Dimensional Modeling
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

## Output
- `results/structures/` — AlphaFold 3 models (PDB format)
- `results/validation/` — ProSA, PROCHECK, QMEANDisCo reports
- `results/md/` — GROMACS trajectories and per-residue analyses
- `results/figures/` — RMSD, RMSF, Rg, SASA, H-bond, ESP plots

## Structure
```
02_modeling_md/
├── data/          # Input sequences
├── scripts/       # Modeling, MD, and analysis scripts
└── results/       # Models, validation, trajectories, figures
```
