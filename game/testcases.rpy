# ===========================================================================
# testcases.rpy  —  SMOKE TEST OTOMATIS
# ===========================================================================
#  Jalankan dengan:
#      ./renpy.sh <folder-proyek> test global --report-detailed
#
#  Tes ini memastikan:
#    - layar nama -> pilih mapel -> kuis berjalan
#    - hint gratis (warm-up) dan hint berbayar memotong kemandirian
#    - 8 soal Indonesia bisa diselesaikan sampai rapor + ending
#    - chapter Jepang tampil dengan UI/dialog Indonesia dan soal Jepang
#      hiragana/katakana + romaji + arti (tanpa kanji)
#    - rumus 8/8 benar + mandiri 20 menghasilkan B
# ===========================================================================
#
#  Catatan headless (tanpa X/GL):
#      RENPY_RENDERER=sw SDL_VIDEODRIVER=dummy SDL_AUDIODRIVER=dummy \
#          ./renpy.sh . test global --report-detailed
#
#  Dua hal wajib supaya node test benar-benar dieksekusi:
#    1. _test.force = True, karena layar main_menu memakai suppress_underlay.
#    2. Paksa redraw tiap tick. Node test dieksekusi di dalam blok gambar;
#       di layar statis (menu) tidak ada redraw, jadi tes akan diam selamanya.
# ===========================================================================

init python:
    _test.force = True

    if renpy.game.args.command == "test":
        def _paksa_redraw():
            if renpy.display.interface is not None:
                renpy.display.interface.force_redraw = True

        config.periodic_callbacks.append(_paksa_redraw)

testsuite global:

    before testcase:
        $ _test.transition_timeout = 0.05
        $ _test.timeout = 15.0
        $ nama_mc = "Rei"

        if not screen "main_menu":
            run MainMenu(confirm=False)

        click "Mulai"
        assert screen "layar_nama" timeout 10.0
        click id "nama_lanjut"

        # Prolog: rumah -> koridor -> kelas, lalu layar pilih kelas tambahan.
        advance until screen "pilih_mapel"

    teardown:
        exit


testcase rumus_nilai:
    $ assert hitung_nilai(8, 8, 20) == 76
    $ assert huruf_nilai(76) == "B"
    $ assert hitung_nilai(8, 8, 100) == 100
    $ assert huruf_nilai(100) == "A"
    $ assert hitung_nilai(0, 8, 100) == 30
    $ assert huruf_nilai(30) == "C"
    $ assert hitung_nilai(7, 8, 100) == 91
    $ assert huruf_nilai(91) == "A"
    $ assert hitung_nilai(4, 8, 100) == 65
    $ assert huruf_nilai(65) == "B"

    # Benar semua tapi mandiri rendah: nilai ditahan di 84 (tetap B).
    $ assert hitung_nilai(8, 8, 54) == 84
    $ assert huruf_nilai(hitung_nilai(8, 8, 54)) == "B"
    $ assert hitung_nilai(8, 8, 55) == 87
    $ assert huruf_nilai(87) == "A"
    $ assert hitung_nilai(7, 8, 0) == 61
    $ assert huruf_nilai(61) == "C"


testcase indonesia_lengkap:
    click id "kartu_id"

    assert eval (mapel_aktif == "id")
    assert eval (bahasa_aktif == "id")

    # Beat guru khas rute Indonesia: Bu Rina tanya kata baku.
    advance until "Mana yang baku"
    assert "Mana yang baku" timeout 10.0
    advance until screen "kuis_soal"

    # Q1 — hint gratis (warm-up)
    click id "hint_buka"
    assert id "hint_0" timeout 10.0
    click id "hint_0"
    advance until screen "kuis_soal"
    assert eval (mandiri == 100)

    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q2 — tanpa hint, lalu interlude koridor
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    # Q3 — hint berbayar termahal
    click id "hint_buka"
    assert id "hint_2" timeout 10.0
    click id "hint_2"
    advance until screen "kuis_soal"
    assert eval (mandiri == 65)

    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q4
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q5
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q6 — lalu interlude kantin + kelas malam
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    # Q7
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q8
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"

    # Hening sebelum nilai keluar (beat cerita sebelum rapor).
    advance until "Yang kamu ngerti"
    assert "Yang kamu ngerti" timeout 10.0

    # Guru membaca hasil, lalu rapor.
    advance until screen "rapor"
    assert eval (benar == 8)
    assert eval (mandiri == 65)
    assert eval (nilai == 90)
    assert eval (huruf == "A")
    click id "rapor_lanjut"

    # Ending A, lalu kembali ke pemilihan mapel.
    advance until screen "akhir_mapel"

    # Ending A tercatat untuk galeri di menu utama.
    assert eval (JUDUL_AKHIR[huruf] == "Yang Memilih")
    assert eval (persistent.akhir_a)

    click id "akhir_ulang"
    assert screen "pilih_mapel" timeout 10.0


testcase nama_bisa_diubah:
    run MainMenu(confirm=False)
    click "Mulai"
    assert screen "layar_nama" timeout 10.0

    click id "nama_input"
    keysym "K_BACKSPACE" repeat 6
    type "Aoi"

    click id "nama_lanjut"
    advance until screen "pilih_mapel"
    assert eval (nama_mc == "Aoi")


testcase ending_b_keluar:
    $ bahasa_aktif = "id"
    $ mapel_aktif = "id"
    $ teks = TEKS_ID
    $ benar = 8
    $ mandiri = 20
    $ total_soal = 8

    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 76)
    assert eval (huruf == "B")
    click id "rapor_lanjut"
    advance until screen "akhir_mapel"
    click id "akhir_keluar"
    assert screen "main_menu" timeout 10.0


testcase ending_c_keluar:
    $ bahasa_aktif = "id"
    $ mapel_aktif = "id"
    $ teks = TEKS_ID
    $ benar = 0
    $ mandiri = 100
    $ total_soal = 8

    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 30)
    assert eval (huruf == "C")
    click id "rapor_lanjut"
    advance until screen "akhir_mapel"
    click id "akhir_keluar"
    assert screen "main_menu" timeout 10.0


testcase jepang_rapor:
    $ bahasa_aktif = "id"
    $ mapel_aktif = "ja"
    $ teks = TEKS_ID
    $ nama_hina = "Hina"
    $ nama_guru_jp = "Sakuraba-sensei"
    $ benar = 7
    $ mandiri = 100
    $ total_soal = 8

    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 91)
    assert eval (huruf == "A")
    assert "Lanjut" timeout 10.0
    click id "rapor_lanjut"

    advance until screen "akhir_mapel"
    assert "Coba mapel lain" timeout 10.0
    click id "akhir_keluar"
    assert screen "main_menu" timeout 10.0


testcase jepang_ending_b:
    $ bahasa_aktif = "id"
    $ mapel_aktif = "ja"
    $ teks = TEKS_ID
    $ nama_guru_jp = "Sakuraba-sensei"
    $ benar = 3
    $ mandiri = 100
    $ total_soal = 8

    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 56)
    assert eval (huruf == "C")
    click id "rapor_lanjut"

    advance until screen "akhir_mapel"
    click id "akhir_ulang"
    assert screen "pilih_mapel" timeout 10.0

    # Cabang B untuk mapel Jepang.
    $ benar = 8
    $ mandiri = 20
    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 76)
    assert eval (huruf == "B")
    click id "rapor_lanjut"
    advance until screen "akhir_mapel"
    click id "akhir_keluar"
    assert screen "main_menu" timeout 10.0


testcase jepang_ending_c:
    $ bahasa_aktif = "id"
    $ mapel_aktif = "ja"
    $ teks = TEKS_ID
    $ nama_guru_jp = "Sakuraba-sensei"
    $ benar = 0
    $ mandiri = 100
    $ total_soal = 8

    run Jump("penilaian")
    advance until screen "rapor"
    assert eval (nilai == 30)
    assert eval (huruf == "C")

    # Nilai C -> lagu ending C.
    pause 2.0
    $ assert renpy.music.get_playing(channel="music") == "audio/bgm_akhir_c.ogg", "akhir=%r" % (renpy.music.get_playing(channel="music"),)

    click id "rapor_lanjut"

    # Ending C: latar kelas malam, Hina kecewa, lalu keluar.
    advance until screen "akhir_mapel"
    click id "akhir_keluar"
    assert screen "main_menu" timeout 10.0


testcase aset_prolog:
    # Nama file apa adanya; beberapa bg memakai tanda hubung dan/atau .jpeg.
    $ assert renpy.loadable("images/bg/rumah.jpg")
    $ assert renpy.loadable("images/bg/bg-kelas_pagi.png")
    $ assert renpy.loadable("images/bg/bg-kelas_sore.png")
    $ assert renpy.loadable("images/bg/bg-kelas_malam.jpeg")
    $ assert renpy.loadable("images/bg/bg-kelas_jadwal.png")
    $ assert renpy.loadable("images/bg/bg-kelas_ramai.jpeg")
    $ assert renpy.loadable("images/bg/bg-koridor-pagi.png")
    $ assert renpy.loadable("images/bg/bg-koridor-sore.png")
    $ assert renpy.loadable("images/bg/koridor-malam.png")
    $ assert renpy.loadable("images/bg/gerbang-malam.png")
    $ assert renpy.loadable("images/bg/bg-kantin_sore.jpeg")
    $ assert renpy.loadable("images/char/ibu_senyum.png")
    $ assert renpy.loadable("images/char/sakuraba_netral.png")
    $ assert renpy.loadable("images/char/sakuraba_puas.png")

    $ assert _aset("bg/rumah", None) == "images/bg/rumah.jpg"
    $ assert _aset("bg/bg-kelas_pagi", None) == "images/bg/bg-kelas_pagi.png"
    $ assert _aset("bg/bg-kelas_sore", None) == "images/bg/bg-kelas_sore.png"
    $ assert _aset("bg/bg-kelas_malam", None) == "images/bg/bg-kelas_malam.jpeg"
    $ assert _aset("bg/bg-kelas_jadwal", None) == "images/bg/bg-kelas_jadwal.png"
    $ assert _aset("bg/bg-kelas_ramai", None) == "images/bg/bg-kelas_ramai.jpeg"
    $ assert _aset("bg/bg-koridor-pagi", None) == "images/bg/bg-koridor-pagi.png"
    $ assert _aset("bg/bg-koridor-sore", None) == "images/bg/bg-koridor-sore.png"
    $ assert _aset("bg/koridor-malam", None) == "images/bg/koridor-malam.png"
    $ assert _aset("bg/gerbang-malam", None) == "images/bg/gerbang-malam.png"
    $ assert _aset("bg/bg-kantin_sore", None) == "images/bg/bg-kantin_sore.jpeg"
    $ assert _aset("char/ibu_senyum", None) == "images/char/ibu_senyum.png"

    # Hina setengah badan: semua ekspresi punya tinggi tampil yang sama.
    $ assert abs(renpy.render(_bust("char/hina_netral", None, 592, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px
    $ assert abs(renpy.render(_bust("char/hina_fokus", None, 429, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px
    $ assert abs(renpy.render(_bust("char/hina_kecewa", None, 429, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px


testcase aset_audio:
    # Musik & efek suara: nama berkas harus persis seperti di 07_audio.rpy.
    $ assert renpy.loadable("audio/bgm_menu.ogg")
    $ assert renpy.loadable("audio/bgm_hari.ogg")
    $ assert renpy.loadable("audio/bgm_kuis.ogg")
    $ assert renpy.loadable("audio/bgm_akhir_a.ogg")
    $ assert renpy.loadable("audio/bgm_akhir_b.ogg")
    $ assert renpy.loadable("audio/bgm_akhir_c.ogg")
    $ assert renpy.loadable("audio/klik.wav")
    $ assert renpy.loadable("audio/benar.wav")
    $ assert renpy.loadable("audio/salah.wav")
    $ assert renpy.loadable("audio/hint.wav")
    $ assert renpy.loadable("audio/blip_rei.wav")
    $ assert renpy.loadable("audio/blip_hina.wav")
    $ assert renpy.loadable("audio/blip_guru.wav")
    $ assert renpy.loadable("audio/blip_ibu.wav")

    # Tiga ekspresi Hina tambahan, tinggi tampil sama dengan yang lain.
    $ assert abs(renpy.render(_bust("char/hina_ketawa+tutupmata", None, 592, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px
    $ assert abs(renpy.render(_bust("char/hina_senyum-tutupmata", None, 592, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px
    $ assert abs(renpy.render(_bust("char/hina_senyum-mulut-terbuka", None, 592, BUST_HINA), 1920, 1080, 0, 0).height - BUST_HINA) <= 1  # pembulatan gambar toleransi 1 px


testcase blip_suara:
    # Kanal "blip" terdaftar dan helper bisa memutar berkasnya tanpa error.
    $ _blip_suara("hina")("show_done")
    $ _blip_suara("guru")("show_done")
    $ _blip_suara("rei")("show_done")
    $ _blip_suara("ibu")("show_done")
    pause 0.1


testcase prolog_cerita:
    run MainMenu(confirm=False)
    click "Mulai"
    assert screen "layar_nama" timeout 10.0
    click id "nama_lanjut"

    # Pamitan di rumah.
    advance until "sarapan dulu"
    assert "sarapan dulu" timeout 10.0

    # Nabrak Hina di koridor, lalu dialog yang diminta.
    advance until "Kamu murid baru ya?"
    assert "Kamu murid baru ya?" timeout 10.0
    advance until "Kelas berapa kamu?"
    assert "Kelas berapa kamu?" timeout 10.0
    advance until "Kita sekelas. Ayo ikut aku, kita udah mau telat."
    assert "Kita sekelas. Ayo ikut aku, kita udah mau telat." timeout 10.0

    # Setelah prolog, layar pilih kelas tambahan muncul.
    advance until screen "pilih_mapel"


testcase menu_indonesia:
    run MainMenu(confirm=False)
    pause 0.5

    assert screen "main_menu" timeout 10.0
    assert "Mulai" timeout 10.0
    assert "Muat" timeout 10.0
    assert "Pengaturan" timeout 10.0
    assert "Tentang" timeout 10.0
    assert "Keluar" timeout 10.0
    assert not "はじめる"
    assert not "ロード"

    click "Mulai"
    assert screen "layar_nama" timeout 10.0
    assert "Lanjut" timeout 10.0
    assert not "名前は？"
    assert not "次へ"


testcase ui_awal_indonesia:
    # Hook sudah berhenti di layar pilih kelas tambahan.
    pause 0.3

    assert screen "pilih_mapel" timeout 10.0
    assert "Bahasa Jepang" timeout 10.0
    assert "Bahasa Indonesia" timeout 10.0
    assert "Kembali" timeout 10.0
    assert not "日本語"


testcase musik:
    # Hook berhenti di layar pilih kelas tambahan (musik menu).
    # Jeda > durasi fade musik (1,5 detik) supaya lagu lama sudah benar-benar hilang.
    pause 2.0
    $ assert renpy.music.get_playing(channel="music") == "audio/bgm_menu.ogg", "peta=%r" % (renpy.music.get_playing(channel="music"),)

    click id "kartu_ja"
    advance until screen "kuis_soal"
    pause 2.0

    # Chapter Jepang memutar lagu kuis, bukan lagu menu.
    $ assert renpy.music.get_playing(channel="music") == "audio/bgm_kuis.ogg", "kuis=%r" % (renpy.music.get_playing(channel="music"),)


testcase jepang_tanpa_kanji:
    # Soal, pilihan, hint, dan penjelasan tidak boleh mengandung kanji.
    $ assert all(not any(u'\u4e00' <= c <= u'\u9fff' for c in (s["tanya"] + " ".join(s["pilihan"]) + " ".join(s["hint"]) + s["penjelasan"])) for s in SOAL_JA)


testcase jepang_lengkap:
    click id "kartu_ja"

    assert eval (mapel_aktif == "ja")

    # Beat guru khas rute Jepang: Sakuraba-sensei minta baca satu kalimat.
    advance until "baca satu kalimat"
    assert "baca satu kalimat" timeout 10.0
    advance until screen "kuis_soal"

    # Q1
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q2 — jawaban benar ada di index 0
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    # Q3
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q4
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q5
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q6 — lalu interlude kantin + kelas malam
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    # Q7
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    # Q8 — soal email terpanjang
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"

    # Hening sebelum nilai keluar (beat cerita sebelum rapor).
    advance until "Sekarang tinggal nunggu"
    assert "Sekarang tinggal nunggu" timeout 10.0

    advance until screen "rapor"
    assert eval (benar == 8)
    assert eval (mandiri == 100)
    assert eval (nilai == 100)
    assert eval (huruf == "A")
    click id "rapor_lanjut"

    advance until screen "akhir_mapel"
    click id "akhir_ulang"
    assert screen "pilih_mapel" timeout 10.0


testcase jepang_smoke:
    click id "kartu_ja"

    assert eval (mapel_aktif == "ja")
    assert eval (bahasa_aktif == "id")
    advance until screen "kuis_soal"
    assert "Tanya Hina" timeout 10.0

    # Hint gratis di soal pertama.
    click id "hint_buka"
    assert id "hint_0" timeout 10.0
    click id "hint_0"
    advance until screen "kuis_soal"

    # Jawaban benar pertama (index 0).
    click id "pilihan_0"
    advance until screen "penjelasan"
    assert "Lanjut" timeout 10.0
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0






testcase saveload_kuis:
    # Simpan di tengah soal, keluar ke menu, muat lagi, lanjutkan kuis.
    click id "kartu_id"
    advance until screen "kuis_soal"

    # Q1 + Q2 benar (tanpa hint).
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    advance until screen "kuis_soal"

    # Q3: hint termahal (mandiri 100 -> 65), lalu simpan di tengah soal.
    click id "hint_buka"
    assert id "hint_2" timeout 10.0
    click id "hint_2"
    advance until screen "kuis_soal"
    $ assert mandiri == 65, "mandiri sebelum simpan = %r" % (mandiri,)
    $ assert benar == 2, "benar sebelum simpan = %r" % (benar,)

    $ renpy.save("uji_saveload")

    run MainMenu(confirm=False)
    assert screen "main_menu" timeout 10.0

    $ renpy.load("uji_saveload")
    pause 0.5

    assert screen "kuis_soal" timeout 10.0
    $ assert mandiri == 65, "mandiri setelah muat = %r" % (mandiri,)
    $ assert benar == 2, "benar setelah muat = %r" % (benar,)

    # Kuis tetap bisa dilanjutkan.
    click id "pilihan_0"
    advance until screen "penjelasan"
    click id "penjelasan_lanjut"
    assert screen "kuis_soal" timeout 10.0

    $ renpy.unlink_save("uji_saveload")


testcase kantin_benar:
    $ benar = 6
    $ mandiri = 100

    run Jump("interlude_kantin")
    advance until "Enam dari enam"
    assert "Enam dari enam." timeout 10.0
    run MainMenu(confirm=False)
    assert screen "main_menu" timeout 10.0


testcase kantin_salah:
    $ benar = 4
    $ mandiri = 70

    run Jump("interlude_kantin")
    advance until "Tadi pas salah"
    assert "Tadi pas salah" timeout 10.0
    run MainMenu(confirm=False)
    assert screen "main_menu" timeout 10.0
