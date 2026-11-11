# Optiland Competition Cases

Reproducible optical-design competition notebooks using standalone-optics and Optiland, with parallel CPU and CUDA verification.

Challenges: [Optiland competitions](https://www.optiland.org/competitions).

| Case | Notebook | Local validation | Submission |
| --- | --- | --- | --- |
| Minimize RMS Spot Size | [Executed notebook](cases/minimize-rms-spot/submission.ipynb) | All declared constraints pass; P = 0 | Received — user-confirmed, 2026-11-10 |
| Design an Achromatic Doublet | [Executed notebook](cases/achromatic-doublet/submission.ipynb) | All declared constraints pass; P = 0 | Received — user-confirmed, 2026-11-11 |

Each notebook includes a frozen prescription, pinned dependencies, calculation definitions, executed outputs and source attribution. Local merit values are not official server scores or rankings. Run all cells to reproduce the results.

The first case uses the original standalone-optics candidate generation and CPU/CUDA screening, dense CPU replay, and a separate SciPy RMS refinement. Optiland independently evaluates the final prescription using matched explicit pupil rays. [Validation record](cases/minimize-rms-spot/final-validation.json).

The notebooks retain Optiland's MIT notice and identify the exact standalone-optics source revision. Software copyright and third-party source notices remain with their respective authors.

Submission receipts and numerical verification are separate records. [First-case receipt](cases/minimize-rms-spot/submission-status.json) records the user-reported success screen; no official score has been observed or assigned here.

The second case uses an air-spaced N-BK7/F2 pair on one fixed 588 nm Gaussian image plane. Its local merit is approximately 0.047910. The selected nominal design has center thicknesses of 30.000 and 19.464 mm; the notebook also reports a comparison with a 14 mm thickness cap. The F-C axial Gaussian focus separation is 0.46443 mm, reported separately from the lateral-color objective. These results establish the declared nominal checks, with no tolerance or fabrication certification.

To check stored execution, PNG outputs and publication hygiene before sharing a notebook:

```sh
python tools/verify_notebook.py cases/achromatic-doublet/submission.ipynb
```

This helper does not rerun optical calculations. Reproduce those by running every notebook cell.
