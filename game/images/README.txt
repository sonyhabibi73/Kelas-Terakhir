TARUH ASET ASLI DI SINI
=======================

00_images.rpy mengecek file otomatis lewat fungsi _aset(nama, fallback).
- File images/NAMA.png/jpg/jpeg/webp ada   -> dipakai
- File tidak ada                           -> tampil placeholder (blok warna +
                                             nama + catatan di layar)

Jadi kalau muncul placeholder saat main, berarti gambarnya belum ada.


STATUS ASET (terakhir dicek: sudah lengkap kecuali yang ditandai)
=================================================================

BACKGROUND — 5 dari 5 ada
-------------------------
  bg rumah         -> images/bg/rumah.jpg
  bg kelas sore    -> images/bg/bg-kelas_sore.png   (perhatikan tanda hubung)
  bg koridor       -> images/bg/koridor.png
  bg kantin        -> images/bg/kantin.png
  bg kelas malam   -> images/bg/bg-kelas_malam.png  (perhatikan tanda hubung)

Semua 1920x1080. Nama file harus persis; kalau tidak, placeholder muncul.


SPRITE — HINA 5 ekspresi: semua ada
-----------------------------------
  char hina netral  -> images/char/hina_netral.png   (481x1059)
  char hina senyum  -> images/char/hina_senyum.png   (481x1059)
  char hina fokus   -> images/char/hina_fokus.png    (325x767)
  char hina kaget   -> images/char/hina_kaget.png    (325x767)
  char hina kecewa  -> images/char/hina_kecewa.png   (325x767)

Hina ditampilkan SETENGAH BADAN (kepala sampai pinggang), bukan full body.
Di 00_images.rpy dipakai _bust(nama, fallback, puncak, tinggi):
  - gambar dipotong dari atas sampai `puncak`
  - hasil potongan diskalakan ke `tinggi` piksel (BUST_HINA = 600)
  - netral/senyum puncak 592, fokus/kaget/kecewa puncak 429
Tinggi yang sama untuk semua ekspresi = ukuran Hina tidak berubah-ubah.
Kalau ganti gambar Hina, sesuaikan angka `puncak` (garis pinggang).


SPRITE — IBU 1 ekspresi: ada
----------------------------
  char ibu senyum   -> images/char/ibu_senyum.png   (432x578)


SPRITE — SAKURABA-SENSEI 3 ekspresi: 2 ada, 1 BELUM
---------------------------------------------------
  char sakuraba netral -> images/char/sakuraba_netral.png  (432x578) ADA
  char sakuraba puas   -> images/char/sakuraba_puas.png    (432x578) ADA
  char sakuraba tegas  -> BELUM. Dipakai di ending C mapel Jepang.
                          Butuh images/char/sakuraba_tegas.png


SPRITE — BU RINA 3 ekspresi: SEMUA BELUM
----------------------------------------
  char rina netral -> images/char/rina_netral.png
  char rina tegas  -> images/char/rina_tegas.png
  char rina puas   -> images/char/rina_puas.png
  (guru wanita Indonesia 30-an, batik)
  Dipakai di semua ending mapel Indonesia, jadi saat ini ketiganya
  tampil sebagai placeholder.


FILE EKSTRA (ada di folder, belum dipakai di script)
====================================================
  images/char/hina_senyum-mulut-terbuka.png
  images/char/hina_senyum-tutupmata.png
  images/char/hina_ketawa+tutupmata.png
  images/char/sakuraba.png                     (746x1148, versi besar guru)
  images/char/Gemini_Generated_Image_...jpeg    (art Ibu versi mentah)
  images/bg/pintu.png                           (latar pintu, 1920x1080)

Kalau mau dipakai, tambahkan satu baris image di 00_images.rpy, contoh

    image char hina tertawa = _bust(
        "char/hina_ketawa+tutupmata",
        _ph_char("#d98aa8", "HINA", "tertawa", ""),
        592,
        BUST_HINA,
    )


POSISI SPRITE (transform di 00_images.rpy)
==========================================
  kanan  : xalign 0.86, yalign 1.0
  kiri   : xalign 0.14, yalign 1.0
  tengah : xalign 0.5,  yalign 1.0


CEK OTOMATIS
============
Smoke test memeriksa aset dan seluruh alur cerita:

    ./renpy.sh . test global --report-detailed

Headless (tanpa X/GL):

    RENPY_RENDERER=sw SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
        ./renpy.sh . test global --report-detailed

Testcase aset_prolog gagal kalau ada file aset yang hilang atau salah nama.


CATATAN PENTING
===============
- Format dikenali: .png, .jpg, .jpeg, .webp
- Setiap menambah file gambar, ulangi (restart) game-nya
- Sprite transparan 432x578 (potret) atau 481x1059 / 325x767 (Hina)
