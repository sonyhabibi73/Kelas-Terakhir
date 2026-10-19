# ===========================================================================
# 07_audio.rpy  —  MUSIK & EFEK SUARA
# ===========================================================================
#  Semua berkas ada di game/audio/. Sumber & lisensi: game/audio/README.txt
#  (domain publik / CC0, aman dipakai dan dibagikan).
#
#  Dua fungsi di bawah selalu memeriksa dulu berkasnya ada. Kalau hilang,
#  game tetap jalan tanpa suara — jadi kamu bebas menukar atau menghapus lagu.
#
#  Daftar berkas:
#    bgm_menu.ogg    layar judul + layar pilih mapel
#    bgm_hari.ogg    prolog + interlude (koridor/kantin/kelas malam)
#    bgm_kuis.ogg    chapter Jepang & Indonesia (bagian mengerjakan soal)
#    bgm_akhir_a/b/c.ogg   rapor + ending sesuai huruf nilai
#    klik.wav / benar.wav / salah.wav / hint.wav
# ===========================================================================

init offset = 100


# Volume semua efek suara (klik, benar, salah, hint).
# 1.0 = sekeras berkas aslinya. Turunkan angka ini kalau masih terlalu keras,
# naikkan kalau terlalu pelan. Musik latar tidak terpengaruh.
define PK_VOLUME_SFX = 0.5


init python:

    def putar_musik(nama, fade=1.5):
        """Putar lagu dari game/audio/ berulang-ulang; diam kalau tidak ada."""

        jalur = "audio/" + nama

        if renpy.loadable(jalur):
            renpy.music.play(jalur, channel="music", fadeout=fade, fadein=fade, loop=True)
        else:
            renpy.music.stop(channel="music", fadeout=fade)

    def putar_suara(nama):
        """Bunyi pendek sekali jalan; diam kalau berkasnya tidak ada."""

        jalur = "audio/" + nama

        if renpy.loadable(jalur):
            renpy.sound.play("<%s>" % PK_VOLUME_SFX + jalur, channel="sound")

    # Musik layar judul (dipakai Ren'Py saat main menu tampil).
    if renpy.loadable("audio/bgm_menu.ogg"):
        config.main_menu_music = "audio/bgm_menu.ogg"

    # Bunyi klik halus untuk semua tombol (style button bawaan, jadi semua
    # textbutton/ikon menu cepat ikut). Dimatikan kalau berkasnya tidak ada.
    if renpy.loadable("audio/klik.wav"):
        style.button.activate_sound = "<%s>" % PK_VOLUME_SFX + "audio/klik.wav"
