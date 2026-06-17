# 01 — PROVEAN

## Purpose
Predict whether amino acid substitutions identified in pmrAB, phoPQ, and mgrB have a deleterious effect on protein function using the PROVEAN (Protein Variation Effect Analyzer) tool.

## Methodology
Reference protein sequences for MgrB, PhoP, PhoQ, PmrA, and PmrB were submitted to PROVEAN. For each isolate, amino acid substitutions observed through MEGA protein alignment were added in the "Variants" field using the standard format: original amino acid + position + substituted amino acid. Deletions and insertions use specific formats such as `A10del` or `A10_A11insG`. PROVEAN calculates the functional impact score for each variant, classifying them as **neutral** or **deleterious**.

## Input
- `data/reference_sequences.faa` — Wild-type reference protein sequences for MgrB, PhoP, PhoQ, PmrA, PmrB
- `data/mutations.csv` — Amino acid substitutions per isolate per gene, with PROVEAN classification

## Output
- `results/` — PROVEAN predictions per substitution (deleterious / neutral)

## Reference Sequences

### MgrB (27 aa)
```
MLNVMCDQDVQFFSGICTINKFIPW
```

### PhoP (223 aa)
```
MRVLVVEDNALLRHHLKVQLQELGHQVDAAEDAREADYYLGEHLPDIAIVDLGLPDEDGLSLIRRWRSHDVSLPVLVLTAREGWQDKVEVLSAGADDYVTKPFHIEEVAARMQALLRRNSGLASQVISLPPFQVDLSRRELSVNDQPIKLTAFEYTIMETLIRNRGKVVSKDSLMLQLYPDAELRESHTIDVLMGRLRKKIQAEYPQDVITTVRGQGYLFELR
```

### PhoQ (486 aa)
```
MKGLLRHIFPLSLRVRFLLATAGVVLVLSLAYGMVALVGYSVSFDKTTFRLLRGESNLFYMLARWENGAIDVDIPENLNMESPTVTLIYDEQGKLLWAQRDVPWLAKRIQPEWLKRNGFHEIEADVDSSSMLLRNNHEIQEQLDAIREQDDDSEMTHSVAINLYPATSKMPQLSIVVVDTIPVELKRSYMVWSWFVYVLAANLLLVIPLLWVAAWWSLRPIESLAKEVRELEEHHREKLNPNTTRELTRLVSNLNRLVRSERERYDKYRTTLTDLTHSLKTPLAVMQSTLRSLRGEKISVDEAEPVMLEQISRISQQIGYYLHRASMRSGGTLLSRELHPIAPLLDSLTSALNKVYQRKGVNISLDISPEITFVGEQNDFMEVMGNVLDNACKYCLEFVEVSVRQTTDSHLHILVEDDGPGIPQSQRRAVFDRGQRADTLRPGQGVGLSVAREIVEQYDGEIIAGESLLGGACMEVVFGRQQMEDKQS
```

### PmrA (222 aa)
```
MKILVIEDDALLLQGLILAMQSEGYVCDGVSTAHEAALSLASNHYSLIVLDLGLPDEDGLHFLSRMRREKMTQPVLILTARDTLEDRISGLDTGADDYLVKPFALEELNARIRALLRRHNNQGDNEISVGNLRLNVTRRLVWLGETALDLTPKEYALLSRLMMKAGSPVHREILYNDIYSWDNEPATNTLEVHIHNLREKIGKSRIRTVRGFGYMLANNIDTE
```

### PmrB (462 aa)
```
MALFATETWTMRHRLLLTIGAILVVCQLISVFWLWHESKEQIQLLVASAIEGHNNQKHVEHEVREAVASLLVPSLLIVGLALYISMLAVRKITRPLSRLQSELENRTPDNLTPIVLSESVPEVTAVTTALNQLVSRLNLTLDRERLFTADVAHELRTPLAGLRLHLELLAKVHGMGVDPLIQRLDQMTTSISQLLQLARVGQSFSAGSYQQVLLLDDVVKPLQDELEAMLAQRQQRLLLTDIENEAVVSGDATLIRVILRNLVENAHRYSPEGSTIRVSVKAGLMPVMAVEDEGPGIDEAKSGELSKAFVRMDSRYGGIGLGLSIVTRIAQLHDAQFFLHNRQPGPGVRAWVLFPQRGGQNVSTH
```

## Mutations per Isolate

All five isolates (2D2A, 2D4A.1, 2D4A.2, 2D4B, 5D3D) are polymyxin B resistant (MIC > 64 µg/mL).

### 2D2A
| Gene | Mutations (Neutral) | Mutations (Deleterious) |
|------|-------------------|------------------------|
| mgrB | WT | — |
| phoP | WT | — |
| phoQ | D150G; G479P; R480P; Q482D; M483G; E484R; D485_S488del* | M1_G33del*; F478W; Q481A |
| pmrA | WT | — |
| pmrB | — | R256G |

### 2D4A.1
| Gene | Mutations (Neutral) | Mutations (Deleterious) |
|------|-------------------|------------------------|
| mgrB | IS903B (IS5 family) | — |
| phoP | WT | — |
| phoQ | D150G | M1-G33del* |
| pmrA | WT | — |
| pmrB | A246T; Q360del; N361del; V362del; S363del; T364del; H365del | S192Y |

### 2D4A.2
| Gene | Mutations (Neutral) | Mutations (Deleterious) |
|------|-------------------|------------------------|
| mgrB | IS903B (IS5 family) | — |
| phoP | WT | — |
| phoQ | D150G | — |
| pmrA | WT | — |
| pmrB | A246T; Q356S; R357A; G359V; Q360R; N361T; V362S; S363A; T364del; H365del | F354S; P355R |

### 2D4B
| Gene | Mutations (Neutral) | Mutations (Deleterious) |
|------|-------------------|------------------------|
| mgrB | WT | — |
| phoP | — | R13C; G215C; G217C |
| phoQ | D150G; V477G; G479P; R480P; Q482D; M483G; E484R; D485-S488del* | F478W; Q481A |
| pmrA | WT | — |
| pmrB | D334T; Q336S; Q343S; P344Q; P346Q; V348S; W351R; L353C; F354Y; Q356R; R357S; G358A; Q360V; N361R; V362T; T364A; H365P | R256G; Q331S; A335P; N341T; R342D; R349del; V352G; P355S |

### 5D3D
| Gene | Mutations (Neutral) | Mutations (Deleterious) |
|------|-------------------|------------------------|
| mgrB | L2F; K21L | N3S; V4F; M5S; D7A; Q8_F12del; S14A; G15del; I16del; C17L; T18L |
| phoP | — | G215D |
| phoQ | L11C; D150G; G479A; R480A; Q481S; Q482R; M483W; E484K; D485I; K486N; Q487R; S488V | S12H; L13Y; R14G; V15del; R16F; F17V |
| pmrA | WT | — |
| pmrB | F354Y; Q356R; R357S; G358A; Q360del; N361del; V362del; S363del; T364del; H365del | G201D; L353del; P355S |

## Structure
```
01_provean/
├── data/              # Reference sequences and mutation tables
├── scripts/           # Batch submission and parsing scripts
└── results/           # PROVEAN predictions and summaries
```
