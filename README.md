# Optiland Competition Cases

Reproducible optical-design competition notebooks using standalone-optics and Optiland, with parallel CPU and CUDA verification.

Challenges: [Optiland competitions](https://www.optiland.org/competitions).

| Case | Notebook | Local validation | Submission |
| --- | --- | --- | --- |
| Minimize RMS Spot Size | [Executed notebook](cases/minimize-rms-spot/submission.ipynb) | All declared constraints pass; P = 0 | Pending |

Each notebook includes a frozen prescription, pinned dependencies, calculation definitions, executed outputs and source attribution. Local merit values are not official server scores or rankings. Run all cells to reproduce the results.

The first case uses the original standalone-optics candidate generation and CPU/CUDA screening, dense CPU replay, and a separate SciPy RMS refinement. Optiland independently evaluates the final prescription using matched explicit pupil rays. [Validation record](cases/minimize-rms-spot/final-validation.json).

The public Optiland sample and standalone-optics source retain their MIT notices inside the notebook. Software copyright and third-party source notices remain with their respective authors.
