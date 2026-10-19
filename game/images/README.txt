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


SPRITE — HINA 8 ekspresi: semua ada
-----------------------------------
  char hina netral        -> images/char/hina_netral.png                  (481x1059)
  char hina senyum        -> images/char/hina_senyum.png                  (481x1059)
  char hina senyum-buka   -> images/char/hina_senyum-mulut-terbuka.png    (481x1059)
  char hina senyum-mata   -> images/char/hina_senyum-tutupmata.png        (481x1059)
  char hina tertawa       -> images/char/hina_ketawa+tutupmata.png        (481x1059)
  char hina fokus         -> images/char/hina_fokus.png                   (325x767)
  char hina kaget         -> images/char/hina_kaget.png                   (325x767)
  char hina kecewa        -> images/char/hina_kecewa.png                  (325x767)

Hina ditampilkan SETENGAH BADAN (kepala sampai pinggang), bukan full body.
Di 00_images.rpy dipakai _bust(nama, fallback, puncak, tinggi):
  - gambar dipotong dari atas sampai `puncak`
  - hasil potongan diskalakan ke `tinggi` piksel (BUST_HINA = 600)
  - netral/senyum/tertawa/senyum-* puncak 592, fokus/kaget/kecewa puncak 429
Tinggi yang sama untuk semua ekspresi = ukuran Hina tidak berubah-ubah.
Kalau ganti gambar Hina, sesuaikan angka `puncak` (garis pinggang).

Ganti ekspresi di tengah adegan pakai `show ... with dissolve`, biar tidak
potong keras. Contohnya ada di prolog, interlude kantin, chapter Jepang/
Indonesia, dan ending A/B/C.


SPRITE — IBU 1 ekspresi: ada
----------------------------
  char ibu senyum   -> images/char/ibu_senyum.png   (432x578)


SPRITE — SAKURABA-SENSEI 3 ekspresi: semua ada
----------------------------------------------
  char sakuraba netral -> images/char/sakuraba_netral.png  (432x578)
  char sakuraba puas   -> images/char/sakuraba_puas.png    (432x578)
  char sakuraba tegas  -> images/char/sakuraba_tegas.jpeg  (432x578)


SPRITE — BU RINA 3 ekspresi: semua ada
--------------------------------------
  char rina netral -> images/char/rina_netral.png
  char rina tegas  -> images/char/rina_tegas.png
  char rina puas   -> images/char/rina_puas.png


FILE EKSTRA
===========
Tidak ada lagi. Semua file di images/char dan images/bg sudah dipetakan ke
00_images.rpy dan dipakai di cerita. Tiga ekspresi Hina yang dulu menganggur
(senyum-mulut-terbuka, senyum-tutupmata, ketawa+tutupmata) sekarang dipakai
di prolog, interlude, chapter Jepang/Indonesia, dan ending A/B/C.

Kalau nanti menambah file baru, tambahkan satu baris image di 00_images.rpy,
contoh

    image char hina melambai = _bust(
        "char/hina_melambai",
        _ph_char("#d98aa8", "HINA", "melambai", ""),
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


GUI (BUKAN DI FOLDER INI)
=========================
Aset tampilan game ada di game/gui_pack/ — hasil olahan dari paket
VisualNovelDialogueGUI_PNG di akar proyek:

    box_*.png     kotak dialog per warna (biru/pink/oranye/hijau/ungu/kuning)
    tab_*.png     tab nama per warna, menempel di kiri atas kotak dialog
    pill_*.png    tombol pill (idle/hover/mati/utama) untuk semua layar
    icon_*.png    ikon bulat menu cepat (riwayat, muat, setting, otomatis,
                  lompati, simpan)
    badge_*.png   kotak status dengan bulatan aksen

Palet dan gaya dipakai di 00_gui_pack.rpy (PK_*). Folder sumber tetap
utuh sebagai perpustakaan; jangan diedit langsung.


CATATAN PENTING
===============
- Format dikenali: .png, .jpg, .jpeg, .webp
- Setiap menambah file gambar, ulangi (restart) game-nya
- Sprite transparan 432x578 (potret) atau 481x1059 / 325x767 (Hina)
