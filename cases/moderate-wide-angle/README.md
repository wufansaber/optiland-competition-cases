# Moderate Wide-Angle Lens Optimization

[Executed submission notebook](submission.ipynb) for the [Optiland challenge](https://www.optiland.org/competitions). All six computational cells have stored successful execution outputs. Run every cell to reproduce the pinned-source CPU/CUDA screen and fresh Optiland-based numerical evaluation.

This is a nominal validation benchmark with **poor image quality**. It uses six powered spherical N-BK7/F2 elements, a physical planar entrance stop with 6 mm EPD, four semi-fields through 30 degrees, and equally weighted 486/588/656 nm light on one fixed image plane. The local merit is 4.98216676 with P = 0; no official score or ranking is claimed.

The score uses primary-wavelength chief-ray fractional distortion and the mean sagittal/tangential polychromatic MTF at 20 lp/mm. Complex spectral OTFs are summed before magnitude. Continuous shifted-pupil overlap avoids relying on an unresolved full FFT pupil phase at this one frequency. The 256-to-512 density comparison changes either MTF axis by at most 0.00010967.

The approximately 31-degree chief incidence and the scalar normalized-pupil approximation remain limitations. Full PSF and complete MTF-curve accuracy, production image quality, fabrication and tolerances are not certified. [Independent audit](independent-final-validation.json), [12-test summary](independent-test-summary.json) and [search-stage selection](selection.json) specify their individual scopes.
