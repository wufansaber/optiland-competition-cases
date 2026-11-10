"""Check a stored executed notebook before publication; does not rerun optics."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import struct


def verify(path: Path, forbidden_text: tuple[str, ...] = ()) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    book = json.loads(text)
    if book.get("nbformat") != 4 or not isinstance(book.get("cells"), list):
        raise ValueError("Expected a version 4 notebook.")
    if re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", text):
        raise ValueError("A machine-specific absolute Windows path is present.")
    if any(value in text for value in forbidden_text):
        raise ValueError("A caller-specified forbidden string is present.")
    cells = [cell for cell in book["cells"] if cell.get("cell_type") == "code"]
    counts = [cell.get("execution_count") for cell in cells]
    if not cells or any(type(count) is not int or count <= 0 for count in counts):
        raise ValueError("Every code cell must have a stored positive execution count.")
    if counts != list(range(1, len(cells) + 1)):
        raise ValueError("Stored execution counts must be consecutive and in document order.")
    images = []
    for cell in cells:
        for output in cell.get("outputs", []):
            if output.get("output_type") == "error":
                raise ValueError("A stored error output is present.")
            png = output.get("data", {}).get("image/png")
            if png is None:
                continue
            encoded = "".join(png) if isinstance(png, list) else png
            data = base64.b64decode("".join(encoded.split()), validate=True)
            if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR" or len(data) < 24:
                raise ValueError("A stored PNG output is invalid.")
            width, height = struct.unpack(">II", data[16:24])
            if not width or not height:
                raise ValueError("A stored PNG output has zero dimensions.")
            images.append({"width": width, "height": height})
    return {"passed": True, "file": path.name, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(), "executedCodeCells": len(cells),
            "errorOutputs": 0, "pngOutputs": images,
            "scope": "Stored execution and publication hygiene only; optical calculations are not rerun."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--forbid-text", action="append", default=[],
                        help="Reject this exact string; may be repeated.")
    args = parser.parse_args()
    print(json.dumps(verify(args.notebook, tuple(args.forbid_text)), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
