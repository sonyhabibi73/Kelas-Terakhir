# 「最後の授業」/ Kelas Terakhir

Visual novel pendek tentang satu kelas sore, dua mapel bahasa, dan satu
kesempatan terakhir untuk benar-benar mengerti. Pemain memilih antara
Bahasa Jepang dan Bahasa Indonesia, menjawab 8 soal, dan nilai akhirnya
menentukan salah satu dari tiga ending (A/B/C).

- Versi: 1.0
- Mesin: Ren'Py 8.5.3
- Bahasa: Indonesia (teks), 1920×1080

## Cara menjalankan

### Dari build (tanpa instal Ren'Py)

1. Ekstrak `KelasTerakhir-1.0-pc.zip` (ada di folder
   `KelasTerakhir-1.0-dists/`, satu level di atas folder proyek ini).
2. Windows: jalankan `KelasTerakhir.exe`. Linux: jalankan `KelasTerakhir.sh`.
3. Paket `pc` sudah berisi Windows dan Linux sekaligus. Paket lain
   (`-win`, `-linux`, `-mac`, `-market`) hanya perlu kalau diminta.

### Dari kode sumber

1. Pasang Ren'Py 8.5.x.
2. Jalankan `renpy.sh /path/ke/Belajar`, atau buka Ren'Py Launcher lalu
   pilih proyek **Belajar** dan klik **Launch Project**.

## Kontrol

| Aksi | Tombol |
|---|---|
| Lanjut dialog | klik kiri, Spasi, atau Enter |
| Lewati cepat | tahan Ctrl |
| Buka menu | Esc |
| Layar penuh | Alt+Enter |
| Mundur satu dialog | roda mouse ke atas |

Tombol riwayat, simpan, muat, opsi, auto, dan skip ada di dua kolom ikon
di tepi layar.

## Isi game

- Prolog, lalu pilih mapel: Bahasa Jepang atau Bahasa Indonesia.
- 8 soal pilihan ganda per mapel, setiap jawaban dapat penjelasan.
- Petunjuk berlapis tiga tingkat; memakai petunjuk menurunkan nilai
  kemandirian.
- Nilai akhir = 70% jawaban benar + 30% kemandirian.
  Kalau semua soal benar tetapi kemandirian di bawah 55, nilai ditahan di
  84 supaya paling tinggi hanya B.
- A ≥ 85, B 65–84, C < 65. Tiap huruf punya ending bernama sendiri
  (Yang Memilih / Yang Dibantu / Yang Mengulang), dan kartu akhir
  menampilkan nilai serta predikat.
- Galeri kecil di pojok kanan bawah menu utama mencatat ending yang sudah
  dicapai (misalnya 2/3).
- Setelah ending: ulangi permainan atau keluar.

## Struktur folder

```
game/00_gui_pack.rpy        palet warna, frame, dan style dari paket GUI
game/00_images.rpy          definisi gambar, ukuran sprite, transform posisi
game/01_config.rpy          variabel cerita, rumus nilai, data pemain
game/01_prolog.rpy          prolog dan pilihan mapel
game/02_ui.rpy              semua layar (menu, kuis, rapor, dsb.)
game/03_hina.rpy            interlude, petunjuk, dan dialog Hina
game/04_bahasa_jepang.rpy   alur mapel Bahasa Jepang + 8 soal
game/05_bahasa_indonesia.rpy alur mapel Bahasa Indonesia + 8 soal
game/06_ending.rpy          rapor, tiga ending, layar ulangi
game/07_audio.rpy           pemutar musik/SFX dan pengaturan volume
game/testcases.rpy          18 tes otomatis
game/images/                sprite dan latar
game/audio/                 musik dan efek suara (lihat README.txt)
game/gui_pack/              aset GUI yang sudah dipanggang
```

## Tes

Dari folder proyek, dengan Ren'Py 8.5.x:

```sh
renpy.sh . --lint

RENPY_RENDERER=sw SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
  renpy.sh . test global --report-detailed
```

Hasil terakhir: 18 testcase dan 103 assertion lulus, lint bersih.
Build `pc.zip` juga sudah diuji dengan menjalankan game dari hasil ekstrak.

## Kredit dan lisensi

- **Mesin:** Ren'Py 8.5.3 — MIT, dengan pustaka LGPL.
  <https://www.renpy.org>
- **Musik:** karya Frédéric Chopin, rekaman Aaron Dunn dari koleksi Musopen
  "The Complete Chopin Collection", lisensi CC0 1.0 (public domain).
  <https://archive.org/details/musopen-chopin>
  Rincian per berkas ada di `game/audio/README.txt`.
- **Efek suara:** dibuat sendiri untuk proyek ini dengan Python (numpy),
  bebas dipakai.
- **Aset gambar** (sprite, latar, paket GUI): berasal dari paket yang
  dipakai proyek ini; lisensinya mengikuti paket asal.

Kode proyek ini boleh dipakai untuk tugas, portofolio, atau dikembangkan
lebih lanjut.
