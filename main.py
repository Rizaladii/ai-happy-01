"""ai-happy-01 entry: write the bundled happy image to the output directory.

The image (a small friendly robot and a fluffy orange kitten baking
cupcakes together, laughing, flour on their noses) ships in this
repository as entry.png.b64, one line of base64 holding the whole PNG.
This program decodes it and writes the PNG bytes to
<output_dir>/entry.png, where output_dir comes from MAKEFUN_OUTPUT_DIR
(default /output, matching the grader's contract).

Standard library only, no network, deterministic: the same input bytes
always produce the same output bytes.
"""

import base64
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png.b64"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"bundled image missing: {SOURCE}")
    raw = base64.b64decode(SOURCE.read_text(encoding="ascii").strip(),
                           validate=True)
    if not raw.startswith(PNG_MAGIC):
        raise SystemExit("bundled image is not a whole PNG")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    target.write_bytes(raw)
    # Fail loudly rather than hand the grader a bad file: the written
    # file must be a whole PNG of the exact size we ship.
    written = target.read_bytes()
    if written != raw or not written.startswith(PNG_MAGIC):
        raise SystemExit("written entry.png failed verification")


if __name__ == "__main__":
    main()
