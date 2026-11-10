# Design an Achromatic Doublet

[Executed submission notebook](submission.ipynb) for the [Optiland challenge](https://www.optiland.org/competitions). Run every cell to reproduce the fixed prescription, source screening and numerical checks. The notebook fetches pinned public sources and verifies their hashes.

The local definition uses F-C chief-ray lateral color at 3 degrees and 588 nm centroid RMS at the three prescribed fields, all on one fixed 588 nm Gaussian image plane. F and C are never refocused separately. Centroid lateral color and a single alternative real d-line focus are separate diagnostics. The site's official score and ranking have not been established here.

| Quantity | Local result |
| --- | --- |
| Merit / penalty | 0.04790991 / 0 |
| EFL / f-number | 100.000 mm / f/8 |
| Absolute chief F-C lateral color, 3 degrees | 0.02608 micrometres |
| 588 nm RMS, 0 / 1.5 / 3 degrees | 3.97765 / 2.06396 / 7.51869 micrometres |
| BFD | 80.07865 mm |
| Absolute 588 nm distortion, 3 degrees | 0.05854% |

The selected air-spaced N-BK7/F2 design has center thicknesses 29.99986 and 19.46445 mm under a declared local 30 mm search cap. A [14 mm cap comparison](conventional-ct14.validation.json) achieves local merit 0.08794544. The selected design's F-C axial Gaussian focus separation is 0.46443 mm; lateral-color optimization does not establish broadband diffraction-limited performance. Verification covers nominal optical and solid geometry, without fabrication or tolerance certification.

[Final optical comparison](final-validation.json), [independent audit](independent-final-validation.json), [adversarial test summary](independent-test-summary.json), and [source screening/refinement selection](selection.json) record their respective scopes. The unchanged standalone-optics stage uses a narrow bounded curvature screen with CPU/CUDA comparison and dense CPU replay; a separately identified SciPy stage refines the local RMS/color objective.
