#!/bin/bash

gmx pdb2gmx -f model.pdb -o model_processed.gro -water spce -ignh <<EOF
13
EOF

gmx editconf -f model_processed.gro -o model_newbox.gro -c -d 1.0 -bt cubic

gmx solvate -cp model_newbox.gro -cs spc216.gro -o model_solv.gro -p topol.top

gmx grompp -f ions.mdp -c model_solv.gro -p topol.top -o ions.tpr -maxwarn 5

gmx genion -s ions.tpr -o model_solv_ions.gro -p topol.top -neutral -conc 0.15 -pname NA -nname CL <<EOF
13
EOF

gmx grompp -f minim.mdp -c model_solv_ions.gro -p topol.top -o em.tpr -maxwarn 5

gmx mdrun -v -deffnm em -s em.tpr

gmx grompp -f nvt.mdp -c em.gro -p topol.top -o nvt.tpr -r em.gro -maxwarn 5

gmx mdrun -deffnm nvt -v -s nvt.tpr 

gmx grompp -f npt.mdp -c nvt.gro -t nvt.cpt -p topol.top -o npt.tpr -r em.gro -maxwarn 5

gmx mdrun -deffnm npt -v -s npt.tpr

gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr -maxwarn 5





