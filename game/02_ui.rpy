# ===========================================================================
# 02_ui.rpy  —  ANTARMUKA & MESIN KUIS
# ===========================================================================
#  Semua layar di sini murni Ren'Py screen. Tidak ada file gambar UI.
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
    add Solid("#e0b34c") xpos 0 ypos 0 xsize 14 ysize 1080

    vbox:
        xpos 150
        ypos 210
        spacing 16

        text "KELAS TERAKHIR" size 104 color "#f5efe0"
        text "「最後の授業」" size 30 color "#e0b34c" kerning 8
        text "Satu kelas. Dua bahasa. Satu kesempatan terakhir." size 26 color "#c3ccd4"

    vbox:
        xpos 150
        ypos 610
        spacing 4

        textbutton "Mulai":
            id "menu_mulai"
            action Start()
            xsize 430
            padding (18, 12)
            background Solid("#00000000")
            hover_background Solid("#e0b34c22")
            text_size 32
            text_color "#d8dee6"
            text_hover_color "#ffd27f"
            text_xalign 0.0

        textbutton "Muat":
            action ShowMenu("load")
            xsize 430
            padding (18, 12)
            background Solid("#00000000")
            hover_background Solid("#e0b34c22")
            text_size 32
            text_color "#d8dee6"
            text_hover_color "#ffd27f"
            text_xalign 0.0

        textbutton "Pengaturan":
            action ShowMenu("preferences")
            xsize 430
            padding (18, 12)
            background Solid("#00000000")
            hover_background Solid("#e0b34c22")
            text_size 32
            text_color "#d8dee6"
            text_hover_color "#ffd27f"
            text_xalign 0.0

        textbutton "Tentang":
            action ShowMenu("about")
            xsize 430
            padding (18, 12)
            background Solid("#00000000")
            hover_background Solid("#e0b34c22")
            text_size 32
            text_color "#d8dee6"
            text_hover_color "#ffd27f"
            text_xalign 0.0

        textbutton "Keluar":
            action Quit(confirm=True)
            xsize 430
            padding (18, 12)
            background Solid("#00000000")
            hover_background Solid("#e0b34c22")
            text_size 32
            text_color "#d8dee6"
            text_hover_color "#ffd27f"
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
        background Solid("#0f1720f5")

        vbox:
            spacing 14

            text "Siapa namamu?" size 44 color "#f5efe0"
            text "Nama ini dipakai sebagai nama protagonis. Default: Rei." size 21 color "#a8b3bd"

            null height 8

            frame:
                xfill True
                padding (22, 14)
                background Solid("#17232f")

                input:
                    id "nama_input"
                    value VariableInputValue("nama_mc")
                    length 16
                    pixel_width 800

            null height 8

            hbox:
                xalign 1.0
                spacing 18

                textbutton "Lanjut":
                    id "nama_lanjut"
                    action Return(True)
                    padding (24, 12)
                    background Solid("#e0b34c")
                    hover_background Solid("#ffd27f")
                    text_size 28
                    text_color "#1c2630"
                    text_hover_color "#1c2630"


# ---------------------------------------------------------------------------
# PILIH MAPEL
# ---------------------------------------------------------------------------

screen pilih_mapel():

    modal True

    add "bg kelas sore"
    add Solid("#0a1016cc")
    add Solid("#e0b34c") xpos 0 ypos 0 xsize 14 ysize 1080

    vbox:
        xalign 0.5
        ypos 80
        spacing 8

        text "Pilih kelas tambahan" size 54 color "#f5efe0" xalign 0.5
        text "Bahasa Jepang  /  Bahasa Indonesia" size 28 color "#e0b34c" xalign 0.5
        text "Pilih kelas yang ingin kamu ikuti." size 21 color "#b9c3cc" xalign 0.5

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
        padding (24, 10)
        background Solid("#00000000")
        hover_background Solid("#e0b34c22")
        text_size 26
        text_color "#a8b3bd"
        text_hover_color "#ffd27f"


screen kartu_mapel(kode, judul, subjudul, guru, materi, catatan):

    button:
        id ("kartu_" + kode)
        xsize 540
        ysize 470
        padding (38, 34)
        action Return(kode)
        background Solid("#101820ee")
        hover_background Solid("#182634f5")

        vbox:
            spacing 12

            text subjudul size 21 color "#e0b34c"
            text judul size 52 color "#f5efe0"
            text guru size 28 color "#c3ccd4"

            null height 10

            text materi size 23 color "#a8b3bd"
            text catatan size 20 color "#8f9aa5" xmaximum 450

            null height 16

            text "Pilih  →" size 24 color "#e0b34c"


# ---------------------------------------------------------------------------
# GAUGE MANDIRI
# ---------------------------------------------------------------------------

screen gauge_mandiri(teks):

    frame:
        xalign 1.0
        yalign 0.5
        padding (14, 8)
        background Solid("#0b1118cc")

        hbox:
            spacing 10
            yalign 0.5

            text teks["gauge"] size 19 color "#c3ccd4" yalign 0.5

            bar:
                value mandiri
                range 100
                xsize 170
                ysize 12
                yalign 0.5
                left_bar Solid("#e0b34c")
                right_bar Solid("#ffffff22")

            text "[mandiri]" size 20 color "#f5efe0" yalign 0.5


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
        background Solid("#0f1720ee")

        fixed:
            xsize 1484
            ysize 54

            text teks["nomor"].format(n=nomor, total=total):
                size 24
                color "#e0b34c"
                yalign 0.5

            text soal["kategori"]:
                xpos 320
                size 19
                color "#8f9aa5"
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
        background Solid("#0f1720f2")

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
                    color "#f5efe0"
                    xmaximum 1400

                null height 2

                for i in range(len(soal["pilihan"])):
                    $ isi = "%d.  %s" % (i + 1, soal["pilihan"][i])
                    textbutton isi:
                        id ("pilihan_%d" % i)
                        action Return(i)
                        xfill True
                        padding (20, 11)
                        background Solid("#17232f")
                        hover_background Solid("#22384a")
                        text_size 24
                        text_color "#d8dee6"
                        text_hover_color "#ffd27f"
                        text_xalign 0.0

    # Bar bawah: tombol petunjuk / petunjuk terakhir.
    frame:
        xalign 0.5
        ypos 790
        xsize 1540
        padding (28, 14)
        background Solid("#0f1720ee")

        if hint_dipakai and hint_terakhir:
            vbox:
                spacing 4
                text teks["hint_terakhir_title"] size 17 color "#e0b34c"
                text hint_terakhir size 21 color "#f0d9a0" xmaximum 1450

        elif hint_dipakai:
            text teks["hint_dipakai"] size 21 color "#a8b3bd"

        else:
            hbox:
                spacing 18
                yalign 0.5

                textbutton teks["hint_buka"]:
                    id "hint_buka"
                    action ToggleScreenVariable("tampil_hint")
                    padding (20, 10)
                    background Solid("#e0b34c")
                    hover_background Solid("#ffd27f")
                    text_size 22
                    text_color "#1c2630"
                    text_hover_color "#1c2630"

                text teks["hint_info"] size 19 color "#a8b3bd" yalign 0.5 xmaximum 1150

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
            xsize 820
            padding (36, 30)
            background Solid("#182634")

            vbox:
                spacing 12

                text teks["hint_title"] size 30 color "#f5efe0"
                text teks["hint_info"] size 19 color "#a8b3bd"

                null height 8

                for lv in range(3):
                    textbutton label_hint(teks, lv, gratis):
                        id ("hint_%d" % lv)
                        action Return(("hint", lv))
                        xfill True
                        padding (20, 14)
                        background Solid("#0f1720")
                        hover_background Solid("#22384a")
                        text_size 25
                        text_color "#d8dee6"
                        text_hover_color "#ffd27f"
                        text_xalign 0.0

                null height 4

                textbutton teks["batal"]:
                    action SetScreenVariable("tampil_hint", False)
                    xalign 1.0
                    padding (18, 8)
                    background Solid("#00000000")
                    hover_background Solid("#ffffff18")
                    text_size 21
                    text_color "#a8b3bd"
                    text_hover_color "#ffd27f"


# ---------------------------------------------------------------------------
# PENJELASAN
# ---------------------------------------------------------------------------

screen penjelasan(soal, jawaban_benar, teks):

    modal True

    $ judul = teks["judul_benar"] if jawaban_benar else teks["judul_salah"]
    $ warna_judul = "#8fd18a" if jawaban_benar else "#e08a8a"

    add Solid("#0a1016e0")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1240
        padding (50, 38)
        background Solid("#0f1720f5")

        vbox:
            spacing 14

            text judul size 46 color warna_judul

            text teks["label_jawaban"] size 19 color "#8f9aa5"
            text soal["pilihan"][soal["benar"]] size 28 color "#f5efe0"

            null height 4

            text teks["label_penjelasan"] size 19 color "#8f9aa5"
            text soal["penjelasan"] size 25 color "#d8dee6" xmaximum 1140

            null height 10

            textbutton teks["lanjut"]:
                id "penjelasan_lanjut"
                action Return()
                xalign 1.0
                padding (26, 12)
                background Solid("#e0b34c")
                hover_background Solid("#ffd27f")
                text_size 24
                text_color "#1c2630"
                text_hover_color "#1c2630"


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
        background Solid("#f5efe2")

        vbox:
            spacing 10

            fixed:
                xsize 896
                ysize 76
                text teks["rapor"] size 44 color "#1c2630" yalign 0.5
                text huruf size 72 color warna_huruf xalign 1.0 yalign 0.5

            add Solid("#c9b99a") xsize 896 ysize 2

            text teks["rapor_rumus"] size 18 color "#5d6a75" xmaximum 896

            null height 4

            use baris_rapor(teks["row_benar"], "%d / %d" % (benar, total_soal))
            use baris_rapor(teks["row_mandiri"], "%d" % mandiri)
            use baris_rapor(teks["row_nilai"], "%d" % nilai)
            use baris_rapor(teks["row_eval"], huruf)

            null height 6

            text teks["review_title"] size 22 color "#1c2630"

            viewport:
                ysize 190
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 6

                    if review:
                        for kategori in review:
                            text "•  " + kategori size 20 color "#5d6a75"
                    else:
                        text teks["review_none"] size 20 color "#5d6a75"

            null height 6

            textbutton teks["lanjut"]:
                id "rapor_lanjut"
                action Return()
                xalign 1.0
                padding (26, 12)
                background Solid("#1c2630")
                hover_background Solid("#3b4a58")
                text_size 23
                text_color "#f5efe2"
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
        background Solid("#0f1720f5")

        vbox:
            spacing 14

            text "END" size 20 color "#e0b34c" kerning 8
            text teks["tamat"] size 42 color "#f5efe0"
            text teks["tamat_sub"] size 22 color "#a8b3bd"

            null height 12

            hbox:
                spacing 20

                textbutton teks["ulang"]:
                    id "akhir_ulang"
                    action Return("ulang")
                    padding (26, 13)
                    background Solid("#e0b34c")
                    hover_background Solid("#ffd27f")
                    text_size 24
                    text_color "#1c2630"
                    text_hover_color "#1c2630"

                textbutton teks["keluar"]:
                    id "akhir_keluar"
                    action Return("keluar")
                    padding (26, 13)
                    background Solid("#17232f")
                    hover_background Solid("#22384a")
                    text_size 24
                    text_color "#d8dee6"
                    text_hover_color "#ffd27f"


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
