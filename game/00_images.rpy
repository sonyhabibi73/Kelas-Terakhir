# ===========================================================================
# 00_images.rpy  —  SEMUA ASET VISUAL
# ===========================================================================
#
#  Sebagian gambar masih PLACEHOLDER (blok warna + label). bg rumah dan
#  char ibu senyum sudah memakai aset asli. Nama image-nya sudah final, jadi
#  file cerita tidak perlu disentuh saat aset lain masuk.
#
#  CARA MENGGANTI (pilih salah satu):
#
#   1) Otomatis — taruh file dengan nama yang sama di folder images/:
#
#        images/bg/rumah.png
#        images/bg/kelas_sore.png
#        images/bg/koridor.png
#        images/bg/kantin.png
#        images/bg/kelas_malam.png
#        images/char/hina_netral.png
#        images/char/hina_senyum.png
#        images/char/hina_fokus.png
#        images/char/hina_kaget.png
#        images/char/hina_kecewa.png
#        images/char/sakuraba_netral.png
#        images/char/sakuraba_tegas.png
#        images/char/sakuraba_puas.png
#        images/char/rina_netral.png
#        images/char/rina_tegas.png
#        images/char/rina_puas.png
#        images/char/ibu_senyum.png
#
#      Format .png, .jpg, .jpeg, dan .webp sama-sama dikenali.
#
#   2) Manual — ganti satu baris image di bawah, misalnya:
#
#        image bg kelas sore = "images/bg/kelas_sore.png"
#
#  DAFTAR ASET FINAL
#  -----------------
#  Background (1920x1080):
#    bg rumah        : rumah Rei, ruang makan dan pintu masuk, pagi
#    bg kelas sore   : kelas SMA Jepang sore, meja berderet, jendela kanan
#    bg koridor      : koridor sekolah, locker, lampu neon
#    bg kantin       : kantin sekolah, meja kayu panjang
#    bg kelas malam  : kelas yang sama saat malam, lampu neon
#
#  Sprite (PNG transparan, tinggi ±980 px):
#    char hina netral / senyum / fokus / kaget / kecewa
#    char ibu senyum
#    char sakuraba netral / tegas / puas
#    char rina netral / tegas / puas
# ===========================================================================


init -1 python:

    def _ph_bg(warna, judul, catatan=""):
        """Placeholder background: blok warna + nama aset yang dibutuhkan."""

        return Fixed(
            Solid(warna),
            Solid("#00000033"),
            Text(judul, size=94, color="#ffffffd8", xalign=0.5, yalign=0.40,
                 outlines=[(4, "#000000b0", 0, 0)]),
            Text(catatan, size=30, color="#ffffff98", xalign=0.5, yalign=0.53),
            Text("PLACEHOLDER  /  images/bg/", size=20, color="#ffffff55",
                 xalign=0.5, yalign=0.94),
            xysize=(1920, 1080),
            fit_first=False,
        )

    def _ph_char(warna, nama, ekspresi, catatan=""):
        """Placeholder sprite: blok warna + nama + ekspresi."""

        return Fixed(
            Solid(warna),
            Solid("#00000018"),
            Text(nama, size=56, color="#ffffff", xalign=0.5, yalign=0.06,
                 outlines=[(3, "#00000090", 0, 0)]),
            Text(ekspresi, size=34, color="#ffffffdd", xalign=0.5, yalign=0.14),
            Text(catatan, size=20, color="#ffffff88", xalign=0.5, yalign=0.82),
            Text("PLACEHOLDER  /  images/char/", size=18, color="#ffffff60",
                 xalign=0.5, yalign=0.95),
            xysize=(560, 980),
            fit_first=False,
        )

    def _aset(nama, fallback):
        """Pakai file asli kalau ada; kalau belum ada, pakai placeholder."""

        for ext in ("png", "jpg", "jpeg", "webp"):
            path = "images/%s.%s" % (nama, ext)
            if renpy.loadable(path):
                return path
        return fallback

    def _bust(nama, fallback, puncak, tinggi=600):
        """
        Potret setengah badan: potong gambar dari atas sampai `puncak`,
        lalu skalakan supaya tingginya `tinggi` piksel di layar.

        puncak : tinggi potongan pada gambar asli (kepala sampai pinggang)
        tinggi : tinggi potongan saat tampil; disamakan untuk semua ekspresi
                 supaya ukuran Hina tidak berubah-ubah antar ekspresi.
        """

        for ext in ("png", "jpg", "jpeg", "webp"):
            path = "images/%s.%s" % (nama, ext)
            if renpy.loadable(path):
                lebar, _tinggi = renpy.image_size(path)
                return Transform(
                    path,
                    crop=(0, 0, lebar, puncak),
                    zoom=tinggi * 1.0 / puncak,
                )
        return fallback


# ---------------------------------------------------------------------------
# BACKGROUND (5)
# ---------------------------------------------------------------------------

# File asli: images/bg/bg-kelas_sore.png (dengan dash). Kita map manual.
image bg rumah = _aset(
    "bg/rumah",
    _ph_bg("#6b5a45", "RUMAH — PAGI", "rumah Rei, ruang makan dan pintu masuk"),
)

# File asli: bg-kelas_sore.png di folder images/bg/
# Naming di folder: bg-kelas_sore.png -> key "bg-kelas_sore"
image bg kelas sore = _aset(
    "bg/bg-kelas_sore",
    _ph_bg("#5b6a7a", "KELAS — SORE", "SMA Jepang, meja berderet, jendela sore"),
)

# Belum ada aset koridor/kantin khusus; pakai placeholder.
image bg koridor = _aset(
    "bg/koridor",
    _ph_bg("#5c6570", "KORIDOR", "koridor sekolah, locker, lampu neon"),
)

image bg kantin = _aset(
    "bg/kantin",
    _ph_bg("#7a6a55", "KANTIN", "kantin sekolah, meja kayu panjang"),
)

# File asli: images/bg/bg-kelas_malam.png (dengan dash). Kita map manual.
image bg kelas malam = _aset(
    "bg/bg-kelas_malam",
    _ph_bg("#2b3442", "KELAS — MALAM", "kelas yang sama, malam, lampu neon"),
)


# ---------------------------------------------------------------------------
# SPRITE — IBU (1 ekspresi)
# ---------------------------------------------------------------------------

image char ibu senyum = _aset(
    "char/ibu_senyum",
    _ph_char("#b98a6a", "IBU", "senyum", "ibu Rei, blouse krem, apron hijau, senyum lembut"),
)


# ---------------------------------------------------------------------------
# SPRITE — HINA (5 ekspresi)
# ---------------------------------------------------------------------------
# PNG transparan. Hina tampil setengah badan (kepala sampai pinggang) supaya
# sejajar dengan potret Ibu/Sakuraba; potongan diskalakan ke tinggi yang sama
# untuk semua ekspresi (bust_hina = 600 px di layar).
#   netral/senyum        481x1059 -> pinggang di y=592
#   fokus/kaget/kecewa   325x767  -> pinggang di y=429

define BUST_HINA = 600

image char hina netral = _bust(
    "char/hina_netral",
    _ph_char("#c98fa0", "HINA", "netral", "gadis SMA, rambut panjang, senyum tipis"),
    592,
    BUST_HINA,
)

image char hina senyum = _bust(
    "char/hina_senyum",
    _ph_char("#d98aa8", "HINA", "senyum", "senyum lembut, suportif"),
    592,
    BUST_HINA,
)

image char hina fokus = _bust(
    "char/hina_fokus",
    _ph_char("#c06f8c", "HINA", "fokus", "serius, mata terfokus, menunjuk buku"),
    429,
    BUST_HINA,
)

image char hina kaget = _bust(
    "char/hina_kaget",
    _ph_char("#e29a86", "HINA", "kaget", "mulut agak terbuka, alis naik"),
    429,
    BUST_HINA,
)

image char hina kecewa = _bust(
    "char/hina_kecewa",
    _ph_char("#a97b8c", "HINA", "kecewa", "senyum tipis, mata sedih"),
    429,
    BUST_HINA,
)


# ---------------------------------------------------------------------------
# SPRITE — SAKURABA-SENSEI (3 ekspresi)
# ---------------------------------------------------------------------------

image char sakuraba netral = _aset(
    "char/sakuraba_netral",
    _ph_char("#6f8f6a", "SAKURABA", "netral", "guru pria Jepang 40-an, kacamata"),
)

image char sakuraba tegas = _aset(
    "char/sakuraba_tegas",
    _ph_char("#5c7d58", "SAKURABA", "tegas", "serius, menegur"),
)

image char sakuraba puas = _aset(
    "char/sakuraba_puas",
    _ph_char("#82a37c", "SAKURABA", "puas", "senyum tipis, mengangguk"),
)


# ---------------------------------------------------------------------------
# SPRITE — BU RINA (3 ekspresi)
# ---------------------------------------------------------------------------

image char rina netral = _aset(
    "char/rina_netral",
    _ph_char("#c9a15a", "BU RINA", "netral", "guru wanita Indonesia 30-an, batik"),
)

image char rina tegas = _aset(
    "char/rina_tegas",
    _ph_char("#b8914a", "BU RINA", "tegas", "serius, menjelaskan"),
)

image char rina puas = _aset(
    "char/rina_puas",
    _ph_char("#d9b06a", "BU RINA", "puas", "senyum bangga"),
)


# ---------------------------------------------------------------------------
# POSISI SPRITE
# ---------------------------------------------------------------------------
# kanan/kiri/tengah dipakai di script (show char ... at kanan)

transform kanan:
    xalign 0.86
    yalign 1.0

transform kiri:
    xalign 0.14
    yalign 1.0

transform tengah:
    xalign 0.5
    yalign 1.0