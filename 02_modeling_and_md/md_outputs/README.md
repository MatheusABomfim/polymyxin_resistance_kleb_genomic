# MD Outputs

Per-protein molecular dynamics outputs (mgrb, phop, phoq, pmra, pmrb), each with WT and 5D3D variants. Available files include XVG analyses (RMSD, RMSF, Rg, SASA, H-bonds), contact maps (JPG), PDB/PQR structures, and EPS/XPM plots.

## Files not included in the repository

The following large files were excluded from version control because they exceed GitHub size limits (individual files up to 133 MB, ~970 MB total):

- `*.dx` — APBS electrostatic potential grids (588 MB)
- `*.tga` — raw electrostatic surface renders (184 MB); compressed JPG equivalents are kept where available
- `md_0_1-run.part*.gro` — final MD production snapshots (196 MB), regenerable from the simulation setup in `../md_setup_files/`

These files are available on request from the authors at any time.
