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
# Kotak dialog & tab nama per karakter (aset paket di gui_pack/):
#   Rei (MC)       → biru
#   Hina           → pink
#   Ibu            → oranye
#   Sakuraba      → hijau
#   Bu Rina        → ungu
#   Narasi (tanpa nama) → kuning, dari style.window

default nama_mc      = "Rei"
default nama_hina    = "Hina"
default nama_guru_jp = "Sakuraba-sensei"
default nama_guru_id = "Bu Rina"

# Blip: bunyi pendek tiap baris dialog. Kanal "blip" memakai mixer "sfx",
# jadi ikut slider efek suara di Pengaturan.
init python:

    def _blip_suara(nama, volume=0.4):
        """Bikin callback Character yang memutar audio/blip_<nama>.wav."""

        jalur = "audio/blip_%s.wav" % nama

        def callback(event, **kwargs):
            if event == "show_done" and not renpy.config.skipping:
                if renpy.loadable(jalur):
                    renpy.sound.play(jalur, channel="blip", relative_volume=volume)

        return callback

    renpy.music.register_channel("blip", mixer="sfx", loop=False)


define r    = Character("[nama_mc]",      window_background=pk_kotak("rei"),      namebox_background=pk_tab("rei"),      callback=_blip_suara("rei"))
define h    = Character("[nama_hina]",    window_background=pk_kotak("hina"),     namebox_background=pk_tab("hina"),     callback=_blip_suara("hina"))
define ibu  = Character("Ibu",            window_background=pk_kotak("ibu"),      namebox_background=pk_tab("ibu"),      callback=_blip_suara("ibu"))
define sk   = Character("[nama_guru_jp]", window_background=pk_kotak("sakuraba"), namebox_background=pk_tab("sakuraba"), callback=_blip_suara("guru"))
define rina = Character("[nama_guru_id]", window_background=pk_kotak("rina"),     namebox_background=pk_tab("rina"),     callback=_blip_suara("guru"))


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

# Ending yang pernah dicapai, untuk galeri kecil di menu utama.
default persistent.akhir_a = False
default persistent.akhir_b = False
default persistent.akhir_c = False


# ---------------------------------------------------------------------------
# IDENTITAS ENDING
# ---------------------------------------------------------------------------
#  Dipakai layar rapor, layar penutup, dan galeri di menu utama.

define WARNA_HURUF = {
    "A": "#2f8f4e",
    "B": "#b8860b",
    "C": "#b0413e",
}

define JUDUL_AKHIR = {
    "A": "Yang Memilih",
    "B": "Yang Dibantu",
    "C": "Yang Mengulang",
}

define PENUTUP_AKHIR = {
    "A": "Kamu memilih kata-katanya sendiri, dan kamu bisa menjelaskan alasannya.",
    "B": "Sebagian sudah kamu pahami. Sisanya kamu selesaikan bersama.",
    "C": "Hari ini belum selesai. Besok kamu mulai lagi, satu per satu.",
}


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
    $ putar_musik("bgm_menu.ogg")

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
