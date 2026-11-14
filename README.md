# Make the AI judge happy — ai-happy-01

A small friendly robot and a fluffy orange kitten baking cupcakes together
in a sunny kitchen, both laughing with flour on their noses. Warm, joyful,
and readable at a glance — made to make the AI judge happy.

## How it works

`main.py` (Python 3.13, standard library only, no network) decodes the
bundled image `entry.png.b64` (one line of base64 holding the whole PNG)
and writes the PNG bytes to `<output_dir>/entry.png`, where `output_dir`
comes from `MAKEFUN_OUTPUT_DIR` (default `/output`, matching the
grader's contract). After writing it verifies the written file is a
whole PNG of the exact size shipped, and fails loudly if not.
The program is deterministic: two runs write identical bytes.

The bundled image is 896×597 pixels, 875,632 bytes (PNG) — inside the
gate limits of 1 MiB and 1024×1024.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```
