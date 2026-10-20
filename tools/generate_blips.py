#!/usr/bin/env python3
"""Bikin blip dialog (satu nada pendek per karakter) ke game/audio/.

Blip diputar sekali per baris dialog lewat callback Character di
game/01_config.rpy. Nadanya sengaja pendek dan pelan supaya tidak
mengalahkan musik. Jalankan ulang kalau mau mengganti nada:

    python3 tools/generate_blips.py
"""

import math
import wave
from pathlib import Path

import numpy as np

SR = 48000
DUR = 0.055
PEAK = 0.6

# Nada dasar per karakter. Makin tinggi, makin ringan terdengar.
NADA = {
    "rei": 190.0,
    "hina": 520.0,
    "guru": 300.0,
    "ibu": 380.0,
}

OUT = Path(__file__).resolve().parent.parent / "game" / "audio"


def blip(freq):
    n = int(SR * DUR)
    t = np.arange(n) / SR
    env = np.exp(-t * 85.0)

    nada = np.sin(2 * math.pi * freq * t) + 0.25 * np.sin(4 * math.pi * freq * t)
    noise = np.random.default_rng(7).standard_normal(n) * 0.10
    x = (nada * 0.6 + noise) * env

    # Redam awal dan akhir supaya tidak ada klik.
    fade = int(SR * 0.003)
    x[:fade] *= np.linspace(0, 1, fade)
    x[-fade:] *= np.linspace(1, 0, fade)

    x *= PEAK / (np.max(np.abs(x)) or 1.0)
    return x


def simpan(path, x):
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes(pcm.tobytes())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for nama, freq in NADA.items():
        path = OUT / ("blip_%s.wav" % nama)
        simpan(path, blip(freq))
        print("tulis", path.relative_to(OUT.parent.parent))


if __name__ == "__main__":
    main()
