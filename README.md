# Genomic and in silico mutations analysis of pmrAB, phoPQ, and mgrB in polymyxin-resistance *Klebsiella pneumoniae* recovered from hospital environment surfaces

## Overview
This repository contains data, scripts, and results for the genomic and in silico analysis of two-component regulatory systems (pmrAB, phoPQ) and the mgrB regulator in polymyxin-resistant *K. pneumoniae* isolates from hospital environmental surfaces.

## Repository Structure

```
polymyxin_resistance_kleb_genomic/
├── 01_provean              # PROVEAN deleterious mutation prediction
├── 02_modeling_and_md      # 3D modeling, MD simulations, structural dynamics
├── 03_resistome            # ABRIcate-based antimicrobial resistance gene screening
├── 04_dms_analysis         # Deep mutational scanning (PyRosetta ddG) simulations
└── README.md               # This file
```

## Pipeline
1. **PROVEAN** — Prediction of deleterious amino acid substitutions in pmrAB, phoPQ, mgrB
2. **Modeling + MD** — Strain selection (5D3D), AlphaFold 3 modeling, GROMACS MD simulations, comparative structural dynamics
3. **Resistome** — Homology-based resistome screening via ABRIcate
4. **DMS in silico** — PyRosetta-based Cartesian ΔΔG scanning
