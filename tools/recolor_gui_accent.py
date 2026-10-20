"""Warnai ulang aksen biru bawaan Ren'Py jadi crimson paket.

Ren'Py membawa beberapa gambar jadi dengan aksen biru (#0099cc). Yang masih
terpakai di game ini:

    game/gui/frame.png                bingkai kotak (dialog konfirmasi)
    game/gui/overlay/game_menu.png    latar menu game + garis aksen vertikal
    game/gui/overlay/main_menu.png    latar menu utama + garis aksen vertikal
    game/gui/window_icon.png          ikon jendela/aplikasi

Semua piksel kebiruan diganti dengan crimson, kecerahan aslinya dipertahankan
supaya bayangan dan tepi anti-alias tetap mulus. Berkas yang sudah tidak
kebiruan dilewati, jadi skrip ini aman dijalankan berulang.

Jalankan dengan:

    python3 tools/recolor_gui_accent.py
"""

from __future__ import annotations

import os

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIRU = (0, 153, 204)          # gui.accent_color bawaan Ren'Py
CRIMSON = (186, 70, 76)       # PK_ACCENT di 00_gui_pack.rpy

BERKAS = [
    "game/gui/frame.png",
    "game/gui/overlay/game_menu.png",
    "game/gui/overlay/main_menu.png",
    "game/gui/window_icon.png",
]


def warnai_ulang(relatif):
    path = os.path.join(ROOT, relatif)
    im = Image.open(path).convert("RGBA")
    a = np.asarray(im).astype(np.float32)

    rgb, alpha = a[:, :, :3], a[:, :, 3]
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # Piksel yang jelas condong biru (bukan putih, abu, atau hitam).
    biru = (b > r + 25) & (b > 70) & (alpha > 0)
    jumlah = int(biru.sum())
    if not jumlah:
        print("lewati %s (tidak ada biru)" % relatif)
        return

    # Kecerahan relatif terhadap biru asli, lalu dipetakan ke crimson.
    skala = rgb.mean(axis=2) / (sum(BIRU) / 3.0)
    baru = np.clip(np.array(CRIMSON, dtype=np.float32) * skala[:, :, None], 0, 255)
    rgb[biru] = baru[biru]

    hasil = np.concatenate([rgb, alpha[:, :, None]], axis=2)
    Image.fromarray(hasil.round().astype(np.uint8), "RGBA").save(path)
    print("warnai %s (%d piksel)" % (relatif, jumlah))


if __name__ == "__main__":
    for berkas in BERKAS:
        warnai_ulang(berkas)
