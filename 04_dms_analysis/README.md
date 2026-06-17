# 04 — DMS In Silico Analysis

## Purpose
Predict the impact of identified mutations on protein stability using PyRosetta-based deep mutational scanning (Cartesian ΔΔG).

## Structure
```
04_dms_analysis/
├── pdb/           # Wild-type structure models (mgrb, phop, phoq, pmra, pmrb)
├── scripts/       # PyRosetta DMS pipeline
│   ├── run_dms.py             # Main DMS execution
│   ├── plot_combined.py       # Combined mutation effect plots
│   ├── plot_individual.py     # Per-gene mutation effect plots
│   ├── plot_tcs1.py           # TCS1-specific plotting
│   ├── plot_tcs2.py           # TCS2-specific plotting
│   └── utils_pyrosetta.py     # Core PyRosetta utilities
├── mgrb/          # mgrB results
├── phop/          # PhoP results
├── phoq/          # PhoQ results
├── pmra/          # PmrA results
└── pmrb/          # PmrB results
```

## Requirements
- Python ≥ 3.11
- PyRosetta (academic license, installed via `pyrosetta-installer`)
- Dependencies listed in `requirements.txt`

## Usage
```bash
# Activate environment with PyRosetta installed
python scripts/run_dms.py --structures pdb/ --output . --mutation_list ../02_modeling_md/results/mutations.tsv
```
