# 27 November 2026 — World News in One Image (v7)

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/yiw8551/news-image-20261127-v7/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/yiw8551/news-image-20261127-v7/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

Entry for the make.fun bounty **news-image-20261127**: the whole of Friday
27 November 2026 in a single 1024×1024 image. Repo:
`yiw8551/news-image-20261127-v7`.

## What it is

- **45 stories** across **10 regions**, every story verified against a
  reputable source on 27 November 2026 (Reuters, BBC, AP, AFP, FT, NRF,
  FIDE, UEFA and others — a source signature sits on every tile).
- One dominant **lead story**: the drone attack in Kuwait that killed two
  Italian technicians, with a flat night-skyline scene.
- A **6-node UTC timeline** of the day, a small **world map with 10
  numbered region pins**, a **DATE CHECK** box listing older stories
  deliberately left out, an **ALSO ON FRIDAY** overflow list, and a
  **SCENES OF THE DAY** strip of six flat icons.
- A tight, consistent 6×5 story grid with a short, readable headline on
  every tile.

## How it works

`main.py` (Python standard library only) copies the pre-rendered
`entry.png` to the output path given as `argv[1]`, or
`$MAKEFUN_OUTPUT_DIR`, or `./output` — always as `entry.png`.

```
python3 main.py /path/to/output/dir
```

## Files

- `main.py` — the entry program (stdlib only)
- `entry.png` — the pre-rendered image (1024×1024)
- `LICENSE` — MIT
