# ===========================================================================
# gui_pack.rpy  —  TEMA GUI DARI VisualNovelDialogueGUI_PNG
# ===========================================================================
#  Semua gambar di gui_pack/ berasal dari folder VisualNovelDialogueGUI_PNG
#  (sudah diolah: pill, kotak dialog per warna, tab nama, ikon bulat).
#
#  Bahasa desain paket:
#      - kotak dialog & panel: pill putih + garis tepi berwarna
#      - tab nama           : pill berwarna, menempel di kiri atas kotak
#      - tombol             : pill putih, sorotan cincin crimson
#      - ikon menu cepat    : bulatan putih, sorotan cincin crimson
#      - warna aksen        : crimson #ba464c
#
#  Warna kotak dialog per tokoh (biar penonton langsung tahu siapa yang
#  bicara): Rei biru, Hina pink, Ibu oranye, Sakuraba hijau, Rina ungu,
#  narasi kuning.
# ===========================================================================


init python:

    ## Palet paket ---------------------------------------------------------
    PK_INK = "#1c2630"            # teks di atas pill terang
    PK_MUTED = "#6b7480"          # teks kedua di atas pill terang
    PK_ACCENT = "#ba464c"         # crimson paket
    PK_ACCENT_TERANG = "#d37c9f"  # pink paket
    PK_MATI = "#8b8f96"           # teks tombol nonaktif

    ## Kotak dialog per tokoh ---------------------------------------------
    PK_WARNA = {
        "rei": "blue",
        "hina": "pink",
        "ibu": "orange",
        "sakuraba": "green",
        "rina": "purple",
        "narasi": "yellow",
    }

    def pk_kotak(tokoh):
        """Kotak dialog (frame, siap melar) untuk satu tokoh."""

        return Frame("gui_pack/box_%s.png" % PK_WARNA[tokoh], 56, 56, 56, 56)

    def pk_tab(tokoh):
        """Tab nama (frame) untuk satu tokoh."""

        return Frame("gui_pack/tab_%s.png" % PK_WARNA[tokoh], 32, 30, 32, 30)

    def pk_pill(berkas, tepi=48):
        """Pill dari gui_pack/ sebagai frame (melebar mengikuti isi)."""

        return Frame("gui_pack/%s.png" % berkas, tepi, tepi, tepi, tepi)

    ## Sering dipakai -----------------------------------------------------
    PK_PANEL = pk_pill("box_yellow", 56)
    PK_PANEL_PINK = pk_pill("box_pink", 56)
    PK_PILL = pk_pill("pill_idle")
    PK_PILL_HOVER = pk_pill("pill_hover")
    PK_PILL_MATI = pk_pill("pill_disabled")
    PK_PILL_UTAMA = pk_pill("pill_utama")
    PK_PILL_UTAMA_HOVER = pk_pill("pill_utama_hover")
    PK_PILL_PUTIH = pk_pill("pill_putih")
    PK_BADGE = pk_pill("badge_yellow", 60)


## Gaya untuk layar kustom (02_ui.rpy) #####################################

style pk_panel is frame:
    background PK_PANEL
    padding (44, 34)

style pk_panel_pink is pk_panel:
    background PK_PANEL_PINK

style pk_button is button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    insensitive_background PK_PILL_MATI
    padding (36, 26)

style pk_button_text is button_text:
    color PK_INK
    hover_color PK_ACCENT
    insensitive_color PK_MATI
    size 26

style pk_utama is pk_button:
    background PK_PILL_UTAMA
    hover_background PK_PILL_UTAMA_HOVER

style pk_utama_text is pk_button_text:
    color "#ffffff"
    hover_color "#ffffff"

style pk_judul is text:
    color PK_INK
    size 46

style pk_judul_kecil is text:
    color PK_INK
    size 28


## Gaya bawaan template yang ikut berubah ##################################
## init offset 100 = dijalankan setelah gui.rpy (offset -2) dan screens.rpy
## (offset -1), jadi tulisan di bawah ini yang menang. Dipakai bentuk
## pernyataan style supaya gaya bawaan ikut dibuat kalau belum ada.

init offset = 100

style window:
    xalign 0.5
    xfill False
    xsize 1200
    ysize 288
    yalign 1.0
    yoffset -40
    padding (0, 0)
    background PK_PANEL              # dipakai narasi (tanpa nama)

style say_dialogue:
    color PK_INK
    size 32
    xpos 84
    xsize 1032
    ypos 74

style say_label:
    color "#ffffff"
    size 30

# Tab nama: menempel di kiri atas kotak, melebar mengikuti panjang nama.
style namebox:
    xpos 44
    ypos -32
    xsize None
    ysize 60
    padding (34, 12)
    background None

## Tombol bawaan (menu game, preferensi, konfirmasi, save/load) -----------

## Tombol bawaan (menu game, preferensi, konfirmasi, save/load) -----------
## Padding wajib lega: ujung pill bulat, jadi teks harus dijauhkan dari tepi.

style button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    insensitive_background PK_PILL_MATI
    padding (48, 22)

style button_text:
    idle_color PK_INK
    hover_color PK_ACCENT
    selected_color PK_ACCENT
    insensitive_color PK_MATI

style navigation_button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    padding (48, 22)

style choice_button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    insensitive_background PK_PILL_MATI
    padding (60, 20)

style choice_button_text:
    idle_color PK_INK
    hover_color PK_ACCENT
    insensitive_color PK_MATI

style slot_button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    padding (36, 28)

style slot_button_text:
    idle_color PK_MUTED
    selected_idle_color PK_ACCENT
    selected_hover_color PK_ACCENT

style page_button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    padding (44, 18)

style help_button:
    padding (48, 22)

style confirm_button:
    background PK_PILL
    hover_background PK_PILL_HOVER
    padding (48, 22)

## Check / radio tidak memakai pill (dipakai di layar Preferensi yang
## latarnya gelap), jadi teksnya tetap terang.
style check_button:
    padding (27, 10, 8, 10)

style check_button_text:
    idle_color "#f0e6d2"
    hover_color PK_ACCENT_TERANG

style radio_button:
    padding (27, 10, 8, 10)

style radio_button_text:
    idle_color "#f0e6d2"
    hover_color PK_ACCENT_TERANG


## Gaya label melayang untuk ikon menu cepat ###############################

style pk_tooltip is frame:
    background PK_PILL
    padding (38, 16)

style pk_tooltip_text is text:
    color PK_INK
    size 22
