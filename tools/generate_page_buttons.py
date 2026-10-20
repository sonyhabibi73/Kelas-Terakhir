"""Tombol bulat kecil untuk baris halaman di layar Simpan/Muat.

Menghasilkan tiga berkas di game/gui_pack/:

    bulat_idle.png    64x128  putih polos
    bulat_hover.png   64x128  putih + cincin crimson 4 px
    bulat_aktif.png   64x128  crimson penuh

Ukuran 128x64 (bukan 64x64) sengaja: bagian tengahnya rata, jadi bisa
dipakai sebagai Frame dengan border 32 tanpa gambar melar/miring saat
tombol melebar mengikuti teks ("Otomatis", "Cepat"). Warna sama dengan
pill_idle/pill_hover/pill_utama.

Jalankan dengan:

    python3 tools/generate_page_buttons.py
"""

from __future__ import annotations

import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "game", "gui_pack")

CRIMSON = (186, 70, 76)
PUTIH = (255, 255, 255)

# Digambar 4x lalu diperkecil supaya tepinya halus.
SKALA = 4
LEBAR, TINGGI = 128, 64


def bulat(berkas, isi, garis=None, tebal=0):
    gambar = Image.new("RGBA", (LEBAR * SKALA, TINGGI * SKALA), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gambar)
    draw.rounded_rectangle(
        (0, 0, LEBAR * SKALA - 1, TINGGI * SKALA - 1),
        radius=TINGGI * SKALA // 2,
        fill=isi + (255,),
        outline=(garis + (255,)) if garis else None,
        width=tebal * SKALA,
    )
    gambar = gambar.resize((LEBAR, TINGGI), Image.LANCZOS)
    gambar.save(os.path.join(OUT, berkas))
    print("tulis", os.path.join("game", "gui_pack", berkas))


if __name__ == "__main__":
    bulat("bulat_idle.png", PUTIH)
    bulat("bulat_hover.png", PUTIH, CRIMSON, tebal=4)
    bulat("bulat_aktif.png", CRIMSON)
