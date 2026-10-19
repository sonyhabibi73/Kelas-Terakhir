# ===========================================================================
# 02_ui.rpy  —  ANTARMUKA & MESIN KUIS
# ===========================================================================
#  Semua layar di sini murni Ren'Py screen. Gambar UI (pill, kotak, ikon)
#  berasal dari paket VisualNovelDialogueGUI_PNG via gui_pack/ — lihat
#  00_gui_pack.rpy untuk palet dan gayanya (PK_*).
#
#  Alur satu soal:
#      tampilkan kuis_soal  ->  jawab ATAU pilih satu petunjuk
#      petunjuk             ->  Hina bicara, gauge mandiri turun
#      jawab                ->  penjelasan  ->  kembali ke chapter
# ===========================================================================


# ---------------------------------------------------------------------------
# JUDUL / MAIN MENU
# ---------------------------------------------------------------------------

screen main_menu():

    tag menu
    modal True

    add "bg kelas sore"
    add Solid("#0a1016cc")
    add Solid(PK_ACCENT) xpos 0 ypos 0 xsize 14 ysize 1080

    vbox:
        xpos 150
        ypos 210
        spacing 16

        text "KELAS TERAKHIR" size 104 color "#ffffff"
        text "「最後の授業」" size 30 color PK_ACCENT_TERANG kerning 8
        text "Satu kelas. Dua bahasa. Satu kesempatan terakhir." size 26 color "#c3ccd4"

    vbox:
        xpos 150
        ypos 500
        spacing 10

        textbutton "Mulai":
            id "menu_mulai"
            action Start()
            xsize 430
            padding (52, 24)
            background PK_PILL_UTAMA
            hover_background PK_PILL_UTAMA_HOVER
            text_size 32
            text_color "#ffffff"
            text_hover_color "#ffffff"
            text_xalign 0.0

        textbutton "Muat":
            action ShowMenu("load")
            xsize 430
            padding (52, 24)
            background PK_PILL
            hover_background PK_PILL_HOVER
            text_size 32
            text_color PK_INK
            text_hover_color PK_ACCENT
            text_xalign 0.0

        textbutton "Pengaturan":
            action ShowMenu("preferences")
            xsize 430
            padding (52, 24)
            background PK_PILL
            hover_background PK_PILL_HOVER
            text_size 32
            text_color PK_INK
            text_hover_color PK_ACCENT
            text_xalign 0.0

        textbutton "Tentang":
            action ShowMenu("about")
            xsize 430
            padding (52, 24)
            background PK_PILL
            hover_background PK_PILL_HOVER
            text_size 32
            text_color PK_INK
            text_hover_color PK_ACCENT
            text_xalign 0.0

        textbutton "Keluar":
            action Quit(confirm=True)
            xsize 430
            padding (52, 24)
            background PK_PILL
            hover_background PK_PILL_HOVER
            text_size 32
            text_color PK_INK
            text_hover_color PK_ACCENT
            text_xalign 0.0

    text "Ren'Py  /  v1.0" size 18 color "#ffffff55" xalign 0.98 yalign 0.97


# ---------------------------------------------------------------------------
# LAYAR NAMA
# ---------------------------------------------------------------------------

screen layar_nama():

    modal True

    add "bg rumah"
    add Solid("#0a1016cc")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 940
        padding (54, 44)
        background PK_PANEL

        vbox:
            spacing 14

            text "Siapa namamu?" size 44 color PK_INK
            text "Nama ini dipakai sebagai nama protagonis. Default: Rei." size 21 color PK_MUTED

            null height 8

            frame:
                xfill True
                padding (28, 18)
                background PK_PILL_HOVER

                input:
                    id "nama_input"
                    value VariableInputValue("nama_mc")
                    length 16
                    pixel_width 800
                    color PK_INK

            null height 8

            hbox:
                xalign 1.0
                spacing 18

                textbutton "Lanjut":
                    id "nama_lanjut"
                    action Return(True)
                    padding (52, 24)
                    background PK_PILL_UTAMA
                    hover_background PK_PILL_UTAMA_HOVER
                    text_size 28
                    text_color "#ffffff"
                    text_hover_color "#ffffff"


# ---------------------------------------------------------------------------
# PILIH MAPEL
# ---------------------------------------------------------------------------

screen pilih_mapel():

    modal True

    add "bg kelas sore"
    add Solid("#0a1016cc")
    add Solid(PK_ACCENT) xpos 0 ypos 0 xsize 14 ysize 1080

    vbox:
        xalign 0.5
        ypos 80
        spacing 8

        text "Pilih kelas tambahan" size 54 color "#ffffff" xalign 0.5
        text "Bahasa Jepang  /  Bahasa Indonesia" size 28 color PK_ACCENT_TERANG xalign 0.5
        text "Pilih kelas yang ingin kamu ikuti." size 21 color "#c3ccd4" xalign 0.5

    hbox:
        xalign 0.5
        ypos 320
        spacing 42

        use kartu_mapel(
            "ja",
            "Bahasa Jepang",
            "Kelas Bahasa Jepang",
            "Sakuraba-sensei",
            "Hiragana・Katakana・Romaji",
            "Soal memakai huruf Jepang + romaji + arti. Dialog dalam bahasa Indonesia.",
        )

        use kartu_mapel(
            "id",
            "Bahasa Indonesia",
            "Kelas Bahasa",
            "Bu Rina",
            "Imbuhan・Ejaan・Ragam",
            "Soal dan dialog dalam bahasa Indonesia.",
        )

    textbutton "Kembali":
        action Return("batal")
        xalign 0.5
        ypos 950
        padding (48, 22)
        background PK_PILL
        hover_background PK_PILL_HOVER
        text_size 26
        text_color PK_INK
        text_hover_color PK_ACCENT


screen kartu_mapel(kode, judul, subjudul, guru, materi, catatan):

    button:
        id ("kartu_" + kode)
        xsize 540
        ysize 470
        padding (38, 34)
        action Return(kode)
        background PK_PANEL
        hover_background PK_PILL_HOVER

        vbox:
            spacing 12

            text subjudul size 21 color PK_ACCENT
            text judul size 52 color PK_INK
            text guru size 28 color PK_MUTED

            null height 10

            text materi size 23 color PK_MUTED
            text catatan size 20 color PK_MUTED xmaximum 450

            null height 16

            text "Pilih  →" size 24 color PK_ACCENT


# ---------------------------------------------------------------------------
# GAUGE MANDIRI
# ---------------------------------------------------------------------------

screen gauge_mandiri(teks):

    frame:
        xalign 1.0
        yalign 0.5
        padding (26, 12)
        background PK_PILL_PUTIH

        hbox:
            spacing 12
            yalign 0.5

            text teks["gauge"] size 19 color PK_MUTED yalign 0.5

            bar:
                value mandiri
                range 100
                xsize 170
                ysize 14
                yalign 0.5
                left_bar Solid(PK_ACCENT)
                right_bar Solid("#1c263022")

            text "[mandiri]" size 20 color (PK_ACCENT if mandiri < 55 else PK_INK) yalign 0.5


# ---------------------------------------------------------------------------
# SOAL
# ---------------------------------------------------------------------------

screen kuis_soal(soal, nomor, total, teks, hint_dipakai, gratis, hint_terakhir):

    modal True

    default tampil_hint = False

    add Solid("#0a1016b8")

    # Bar atas: nomor soal, kategori, gauge.
    frame:
        xalign 0.5
        ypos 28
        xsize 1540
        padding (28, 14)
        background PK_PANEL

        fixed:
            xsize 1484
            ysize 54

            text teks["nomor"].format(n=nomor, total=total):
                size 24
                color PK_ACCENT
                yalign 0.5

            text soal["kategori"]:
                xpos 320
                size 19
                color PK_MUTED
                yalign 0.5

            use gauge_mandiri(teks)

    # Pertanyaan + pilihan. Viewport membuat soal panjang (Jepang + romaji
    # + arti) tetap bisa dibaca tanpa menabrak bar petunjuk di bawah.
    frame:
        xalign 0.5
        ypos 118
        xsize 1540
        ysize 650
        padding (36, 20)
        background PK_PANEL

        viewport:
            ysize 610
            xsize 1450
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 12
                xsize 1410

                text soal["tanya"]:
                    size 28
                    color PK_INK
                    xmaximum 1400

                null height 2

                for i in range(len(soal["pilihan"])):
                    $ isi = "%d.  %s" % (i + 1, soal["pilihan"][i])
                    textbutton isi:
                        id ("pilihan_%d" % i)
                        action Return(i)
                        xfill True
                        padding (52, 24)
                        background PK_PILL
                        hover_background PK_PILL_HOVER
                        text_size 24
                        text_color PK_INK
                        text_hover_color PK_ACCENT
                        text_xalign 0.0

    # Bar bawah: tombol petunjuk / petunjuk terakhir.
    frame:
        xalign 0.5
        ypos 790
        xsize 1540
        padding (28, 14)
        background PK_PANEL

        if hint_dipakai and hint_terakhir:
            vbox:
                spacing 4
                text teks["hint_terakhir_title"] size 17 color PK_ACCENT
                text hint_terakhir size 21 color PK_INK xmaximum 1450

        elif hint_dipakai:
            text teks["hint_dipakai"] size 21 color PK_MUTED

        else:
            hbox:
                spacing 18
                yalign 0.5

                textbutton teks["hint_buka"]:
                    id "hint_buka"
                    action ToggleScreenVariable("tampil_hint")
                    padding (48, 22)
                    background PK_PILL_UTAMA
                    hover_background PK_PILL_UTAMA_HOVER
                    text_size 22
                    text_color "#ffffff"
                    text_hover_color "#ffffff"

                text teks["hint_info"] size 19 color PK_MUTED yalign 0.5 xmaximum 1150

    # Popup pilih satu petunjuk.
    if tampil_hint and not hint_dipakai:

        # Lapisan gelap ini juga menahan klik agar tidak jatuh ke pilihan
        # jawaban di belakang popup.
        button:
            xsize 1920
            ysize 1080
            action NullAction()
            background Solid("#000000b0")
            hover_background Solid("#000000b0")

        frame:
            xalign 0.5
            yalign 0.5
            xsize 900
            padding (44, 36)
            background PK_PANEL_PINK

            vbox:
                spacing 12

                text teks["hint_title"] size 30 color PK_INK
                text teks["hint_info"] size 19 color PK_MUTED

                null height 8

                for lv in range(3):
                    textbutton label_hint(teks, lv, gratis):
                        id ("hint_%d" % lv)
                        action Return(("hint", lv))
                        xfill True
                        padding (48, 22)
                        background PK_PILL
                        hover_background PK_PILL_HOVER
                        text_size 25
                        text_color PK_INK
                        text_hover_color PK_ACCENT
                        text_xalign 0.0

                null height 4

                textbutton teks["batal"]:
                    action SetScreenVariable("tampil_hint", False)
                    xalign 1.0
                    padding (44, 18)
                    background PK_PILL
                    hover_background PK_PILL_HOVER
                    text_size 21
                    text_color PK_MUTED
                    text_hover_color PK_ACCENT


# ---------------------------------------------------------------------------
# PENJELASAN
# ---------------------------------------------------------------------------

screen penjelasan(soal, jawaban_benar, teks):

    modal True

    $ judul = teks["judul_benar"] if jawaban_benar else teks["judul_salah"]
    $ warna_judul = "#2f8f4e" if jawaban_benar else "#b0413e"

    add Solid("#0a1016e0")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1240
        padding (50, 38)
        background PK_PANEL

        vbox:
            spacing 14

            text judul size 46 color warna_judul

            text teks["label_jawaban"] size 19 color PK_MUTED
            text soal["pilihan"][soal["benar"]] size 28 color PK_INK

            null height 4

            text teks["label_penjelasan"] size 19 color PK_MUTED
            text soal["penjelasan"] size 25 color PK_INK xmaximum 1140

            null height 10

            textbutton teks["lanjut"]:
                id "penjelasan_lanjut"
                action Return()
                xalign 1.0
                padding (52, 24)
                background PK_PILL_UTAMA
                hover_background PK_PILL_UTAMA_HOVER
                text_size 24
                text_color "#ffffff"
                text_hover_color "#ffffff"


# ---------------------------------------------------------------------------
# RAPOR
# ---------------------------------------------------------------------------

screen baris_rapor(label, isi):

    fixed:
        xsize 880
        ysize 34

        text label size 23 color "#5d6a75" yalign 0.5
        text isi size 23 color "#1c2630" xalign 1.0 yalign 0.5


screen rapor(teks):

    modal True

    $ review = daftar_review(hasil)
    $ warna_huruf = "#2f8f4e" if huruf == "A" else ("#b8860b" if huruf == "B" else "#b0413e")

    add Solid("#0a1016e6")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        padding (52, 40)
        background PK_PANEL

        vbox:
            spacing 10

            fixed:
                xsize 896
                ysize 76
                text teks["rapor"] size 44 color PK_INK yalign 0.5
                text huruf size 72 color warna_huruf xalign 1.0 yalign 0.5

            add Solid("#e3bb72") xsize 896 ysize 2

            text teks["rapor_rumus"] size 18 color PK_MUTED xmaximum 896

            null height 4

            use baris_rapor(teks["row_benar"], "%d / %d" % (benar, total_soal))
            use baris_rapor(teks["row_mandiri"], "%d" % mandiri)
            use baris_rapor(teks["row_nilai"], "%d" % nilai)
            use baris_rapor(teks["row_eval"], huruf)

            null height 6

            text teks["review_title"] size 22 color PK_INK

            viewport:
                ysize 190
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 6

                    if review:
                        for kategori in review:
                            text "•  " + kategori size 20 color PK_MUTED
                    else:
                        text teks["review_none"] size 20 color PK_MUTED

            null height 6

            textbutton teks["lanjut"]:
                id "rapor_lanjut"
                action Return()
                xalign 1.0
                padding (52, 24)
                background PK_PILL_UTAMA
                hover_background PK_PILL_UTAMA_HOVER
                text_size 23
                text_color "#ffffff"
                text_hover_color "#ffffff"


# ---------------------------------------------------------------------------
# LAYAR PENUTUP
# ---------------------------------------------------------------------------

screen akhir_mapel(teks):

    modal True

    add Solid("#0a1016dd")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        padding (50, 42)
        background PK_PANEL

        vbox:
            spacing 14

            text "END" size 20 color PK_ACCENT kerning 8
            text teks["tamat"] size 42 color PK_INK
            text teks["tamat_sub"] size 22 color PK_MUTED

            null height 12

            hbox:
                spacing 20

                textbutton teks["ulang"]:
                    id "akhir_ulang"
                    action Return("ulang")
                    padding (52, 24)
                    background PK_PILL_UTAMA
                    hover_background PK_PILL_UTAMA_HOVER
                    text_size 24
                    text_color "#ffffff"
                    text_hover_color "#ffffff"

                textbutton teks["keluar"]:
                    id "akhir_keluar"
                    action Return("keluar")
                    padding (52, 24)
                    background PK_PILL
                    hover_background PK_PILL_HOVER
                    text_size 24
                    text_color PK_INK
                    text_hover_color PK_ACCENT


# ---------------------------------------------------------------------------
# MESIN SATU SOAL
# ---------------------------------------------------------------------------

label satu_soal(daftar, i, teks):

    $ soal = daftar[i]
    $ total_soal = len(daftar)
    $ hint_dipakai = False
    $ hint_terakhir = ""
    $ gratis = (i < 2)
    $ jawab = -1

    while jawab < 0:

        call screen kuis_soal(soal, i + 1, total_soal, teks, hint_dipakai, gratis, hint_terakhir)

        if isinstance(_return, tuple) and _return[0] == "hint":

            $ level = _return[1]
            call hina_hint(level, soal, gratis)
            $ hint_dipakai = True
            $ hint_terakhir = soal["hint"][level]

        else:
            $ jawab = _return

    $ jawaban_benar = (jawab == soal["benar"])

    if jawaban_benar:
        $ benar = benar + 1
        $ pesan = teks["benar"]
        show char hina senyum at kanan
        h "[pesan]"
    else:
        $ pesan = teks["salah"]
        show char hina kaget at kanan
        h "[pesan]"

    $ hasil.append({
        "no": i + 1,
        "kategori": soal["kategori"],
        "benar": jawaban_benar,
        "hint": 1 if hint_dipakai else 0,
    })

    call screen penjelasan(soal, jawaban_benar, teks)

    show char hina netral at kanan
    return
