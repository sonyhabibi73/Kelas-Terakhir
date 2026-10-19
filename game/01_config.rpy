# ===========================================================================
# 01_config.rpy  —  IDENTITAS, VARIABEL, DAN RUMUS
# ===========================================================================
#  MC  : Rei (first person, tanpa sprite)
#  Hina: teman sekelas, duduk di sebelah Rei
#  Ibu : ibu Rei, hanya suara (tanpa sprite)
#  Guru: Sakuraba-sensei / Bu Rina Hartati
# ===========================================================================


# ---------------------------------------------------------------------------
# KARAKTER
# ---------------------------------------------------------------------------
# Textbox per karakter:
#   Rei (MC)       → textbox_light_blue.png
#   Hina           → textbox_light_pink.png
#   Ibu, Sakuraba, Bu Rina → textbox.png (default)

default nama_mc      = "Rei"
default nama_hina    = "Hina"
default nama_guru_jp = "Sakuraba-sensei"
default nama_guru_id = "Bu Rina"

define r    = Character("[nama_mc]",      color="#c9dcff", window_background="gui/textbox.png")
define h    = Character("[nama_hina]",    color="#ff799f", window_background="gui/textbox.png")
define ibu  = Character("Ibu",            color="#e8c9a0", window_background="gui/textbox.png")
define sk   = Character("[nama_guru_jp]", color="#bfe3a6", window_background="gui/textbox.png")
define rina = Character("[nama_guru_id]", color="#ffd9a0", window_background="gui/textbox.png")


# ---------------------------------------------------------------------------
# VARIABEL PERMAINAN
# ---------------------------------------------------------------------------

default bahasa_aktif = "id"      # bahasa UI/dialog; kedua mapel memakai Indonesia
default mapel_aktif  = "id"      # mapel yang dipilih: "ja" atau "id"
default teks         = {}        # diisi TEKS_ID oleh chapter

default mandiri      = 100       # 自主力 / kemandirian
default benar        = 0         # jumlah jawaban benar
default hasil        = []        # catatan tiap soal
default nilai        = 0
default huruf        = "C"
default total_soal   = 8

default soal           = {}
default jawab          = -1
default gratis         = False
default hint_dipakai   = False
default hint_terakhir  = ""
default jawaban_benar  = False


# ---------------------------------------------------------------------------
# FUNGSI & RUMUS
# ---------------------------------------------------------------------------

init python:

    # Biaya memilih satu jenis petunjuk: arahan / strategi / hampir jawaban.
    BIAYA_HINT = (10, 20, 35)

    def biaya_hint(level, gratis=False):
        """Biaya petunjuk tingkat level (0..2). Warm-up = gratis."""
        if gratis:
            return 0
        if level < 0 or level >= len(BIAYA_HINT):
            return 0
        return BIAYA_HINT[level]

    def label_hint(teks, level, gratis):
        """Teks tombol petunjuk: nama tingkat + harga."""
        biaya = biaya_hint(level, gratis)
        if biaya == 0:
            harga = teks["gratis"]
        else:
            harga = teks["harga"].format(biaya=biaya)
        return "%s  /  %s" % (teks["hint_level"][level], harga)

    def mulai_sesi(mapel):
        """Reset state sebelum satu mapel dimulai."""
        # Kedua mapel memakai narasi/UI bahasa Indonesia.
        # Soal bahasa Jepang tetap memakai huruf Jepang + romaji + arti.
        store.bahasa_aktif = "id"
        store.mapel_aktif = mapel
        store.mandiri = 100
        store.benar = 0
        store.hasil = []
        store.nilai = 0
        store.huruf = "C"
        store.total_soal = 8
        store.hint_dipakai = False
        store.hint_terakhir = ""

        store.nama_hina = "Hina"

        if mapel == "ja":
            store.nama_guru_jp = "Sakuraba-sensei"
        else:
            store.nama_guru_id = "Bu Rina"

    def hitung_nilai(jml_benar, total, jml_mandiri):
        """
        nilai = 0.7 * (benar/total*100) + 0.3 * mandiri.

        Kalau semua soal benar tapi kemandirian rendah (< 55), nilai
        ditahan di 84: menjawab benar tanpa usaha sendiri paling tinggi B.
        """
        if total <= 0:
            return 0
        skor_soal = jml_benar * 100.0 / total
        n = int(0.7 * skor_soal + 0.3 * jml_mandiri + 0.5)
        if jml_benar >= total and jml_mandiri < 55:
            n = min(n, 84)
        return max(0, min(100, n))

    def huruf_nilai(n):
        """A >= 85, B 65-84, C < 65."""
        if n >= 85:
            return "A"
        if n >= 65:
            return "B"
        return "C"

    def daftar_review(hasil):
        """Kategori soal yang masih salah, tanpa duplikat."""
        daftar = []
        for baris in hasil:
            if (not baris["benar"]) and (baris["kategori"] not in daftar):
                daftar.append(baris["kategori"])
        return daftar


# ---------------------------------------------------------------------------
# ALUR AWAL
# ---------------------------------------------------------------------------

label awal_permainan:

    # Layar nama. Default "Rei"; pemain boleh mengganti.
    call screen layar_nama

    $ nama_mc = nama_mc.strip().replace("{", "").replace("}", "").replace("[", "").replace("]", "")
    if not nama_mc:
        $ nama_mc = "Rei"

    # Prolog cerita: rumah -> koridor -> kelas, lalu pilih kelas tambahan.
    jump prolog


label pilih_mapel:

    $ quick_menu = True

    scene bg kelas sore with fade
    call screen pilih_mapel

    if _return == "ja":
        $ mulai_sesi("ja")
        jump chapter_jepang

    elif _return == "id":
        $ mulai_sesi("id")
        jump chapter_indonesia

    # Tombol kembali di layar pemilihan mapel.
    return
