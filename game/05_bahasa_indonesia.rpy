# ===========================================================================
# 05_bahasa_indonesia.rpy  —  CHAPTER BAHASA INDONESIA
# ===========================================================================
#  Semua string di chapter ini berbahasa Indonesia: UI, soal, hint,
#  penjelasan, dialog Hina, dan dialog guru.
# ===========================================================================


define TEKS_ID = {
    "nomor":              "Soal {n} dari {total}",
    "gauge":              "Kemandirian",
    "hint_buka":          "Tanya Hina",
    "gratis":             "gratis",
    "harga":              "-{biaya}",
    "hint_title":         "Petunjuk dari Hina",
    "hint_level":         ("Arahan", "Strategi", "Hampir jawaban"),
    "hint_info":          "Maksimal satu petunjuk per soal. Petunjuk yang lebih tajam memotong kemandirian lebih besar.",
    "hint_terakhir_title": "Petunjuk yang dipakai",
    "hint_dipakai":       "Petunjuk untuk soal ini sudah dipakai.",
    "batal":              "Batal",
    "benar":              "Benar! Bagus.",
    "salah":              "Belum tepat. Yuk cek alasannya.",
    "judul_benar":        "Benar",
    "judul_salah":        "Belum tepat",
    "label_jawaban":      "Jawaban yang tepat",
    "label_penjelasan":   "Penjelasan",
    "lanjut":             "Lanjut",
    "rapor":              "Rapor",
    "rapor_rumus":        "Nilai akhir = ketepatan jawaban × 0.7 + kemandirian × 0.3",
    "row_benar":          "Jawaban benar",
    "row_mandiri":        "Kemandirian",
    "row_nilai":          "Nilai akhir",
    "row_eval":           "Predikat",
    "review_title":       "Materi untuk diulang",
    "review_none":        "Tidak ada materi yang perlu diulang.",
    "ulang":              "Coba mapel lain",
    "keluar":             "Keluar",
    "tamat_sub":          "Sampai jumpa di mapel lain.",
}


# ---------------------------------------------------------------------------
# BANK SOAL — 8 SOAL
# ---------------------------------------------------------------------------

define SOAL_ID = [

    {
        "kategori": "Imbuhan meN-",
        "tanya": "Pilihlah pasangan kata yang penulisannya benar!",
        "pilihan": ["menyapu, mencuci", "mensapu, menyuci", "menyapu, menyuci", "mensapu, mencuci"],
        "benar": 0,
        "penjelasan": "Imbuhan meN- berubah bergantung pada huruf awal kata dasar. Huruf k, p, t, dan s luluh (menyapu, memukul, menulis, mengirim), sedangkan huruf c dan huruf lain tidak luluh (mencuci, menggambar, membaca).",
        "hint": [
            "Ingat kembali pelajaran imbuhan meN-: bentuk imbuhan ditentukan huruf pertama kata dasar.",
            "Huruf s pada kata sapu luluh menjadi meny- (menyapu). Huruf c pada kata cuci tidak luluh (mencuci).",
            "Cari pilihan yang memuat menyapu dan mencuci sekaligus. Pilihan lain pasti salah satu katanya keliru.",
        ],
    },

    {
        "kategori": "Kata baku",
        "tanya": "Manakah kelompok kata yang SELURUHNYA baku?",
        "pilihan": ["apotek, izin, aktif", "apotik, ijin, aktip", "apotek, ijin, aktip", "apotik, izin, aktif"],
        "benar": 0,
        "penjelasan": "Menurut KBBI, bentuk baku adalah apotek (bukan apotik), izin (bukan ijin), dan aktif (bukan aktip). Bentuk tidak baku biasanya muncul dari kebiasaan pengucapan sehari-hari.",
        "hint": [
            "Tiga kata kunci: apotek, izin, aktif. Bandingkan dengan bentuk di KBBI.",
            "Bentuk tidak baku: apotik, ijin, aktip. Buang semua pilihan yang memuatnya.",
            "Tersisa dua pilihan tanpa apotik. Sekarang buang yang masih memuat ijin.",
        ],
    },

    {
        "kategori": "Konjungsi",
        "tanya": "Dia pandai berbicara, (...) adiknya lebih pandai menulis.　Konjungsi yang tepat untuk bagian rumpang adalah ...",
        "pilihan": ["sedangkan", "tetapi", "melainkan", "sehingga"],
        "benar": 0,
        "penjelasan": "Konjungsi sedangkan mempertentangkan dua hal atau dua subjek yang berbeda. Kata tetapi dipakai untuk pertentangan dalam satu subjek yang sama, melainkan dipakai setelah penyangkalan (bukan ... melainkan ...), dan sehingga menyatakan akibat.",
        "hint": [
            "Lihat subjek di kiri dan kanan: Dia dan adiknya. Ada dua orang yang berbeda, bukan satu.",
            "Kata tetapi cocok bila subjeknya sama (Dia rajin, tetapi sering lupa). Kalau dua subjek dibandingkan, konjungsinya lain.",
            "Pilihan tinggal sedangkan atau tetapi. Subjek kiri dan kanan berbeda, jadi kata yang tepat adalah?",
        ],
    },

    {
        "kategori": "Imbuhan peN-",
        "tanya": "Imbuhan peN- pada kata penyapu menunjukkan bahwa kata dasarnya berawalan huruf ...",
        "pilihan": ["s", "ny", "p", "c"],
        "benar": 0,
        "penjelasan": "Bentuk peny- dipakai jika kata dasarnya berawalan huruf s yang luluh menjadi ny: sapu menjadi penyapu, sewa menjadi penyewa, siar menjadi penyiar. Huruf p luluh menjadi m (pukul menjadi pemukul), dan huruf c tetap (cuci menjadi pencuci). Bunyi ny bukan huruf awal kata dasar, melainkan hasil peluluhan.",
        "hint": [
            "Buka kembali aturan imbuhan peN-: bentuk imbuhan menyesuaikan huruf pertama kata dasar.",
            "Bentuk peny- dipakai sebelum kata dasar berawalan s. Contoh lain: sewa menjadi penyewa.",
            "Bunyi ny bukan huruf awal kata dasar, tetapi hasil peluluhan. Jadi huruf aslinya adalah?",
        ],
    },

    {
        "kategori": "Ragam bahasa formal",
        "tanya": "Ubahlah kalimat ini menjadi ragam formal: 『Besok aku nggak bisa datang, ya.』",
        "pilihan": [
            "Besok saya tidak dapat datang.",
            "Besok aku tidak dapat hadir.",
            "Besok saya nggak bisa datang.",
            "Besok saya tidak bisa datang ya.",
        ],
        "benar": 0,
        "penjelasan": "Ragam formal menghindari kata dan partikel percakapan seperti aku, nggak, dan ya, serta memakai bentuk baku: saya dan tidak dapat. Kalimat formal juga tidak memakai partikel penegas di akhir kalimat.",
        "hint": [
            "Tandai dulu kata yang tidak formal di kalimat itu: aku, nggak, dan ya.",
            "aku berubah menjadi saya; nggak berubah menjadi tidak; partikel ya di akhir kalimat dihapus.",
            "Dua pilihan sudah memakai saya. Buang yang masih memakai partikel percakapan ya.",
        ],
    },

    {
        "kategori": "Kelas kata",
        "tanya": "Pada kalimat 『Ani pergi ke pasar di pagi hari』, kata ke dan di termasuk ...",
        "pilihan": ["kata depan (preposisi)", "kata sambung (konjungsi)", "kata sifat", "kata kerja"],
        "benar": 0,
        "penjelasan": "Kata depan atau preposisi (di, ke, dari, pada) menandai hubungan tempat, arah, atau waktu. Kata sambung menghubungkan klausa atau kalimat, misalnya dan, tetapi, karena, sehingga.",
        "hint": [
            "Perhatikan fungsi kedua kata itu: menunjukkan arah dan waktu.",
            "Kata depan atau preposisi: di, ke, dari, pada. Kata sambung: dan, tetapi, karena.",
            "Jawabannya bukan kata sambung. Pilih istilah untuk kata yang menandai arah dan waktu.",
        ],
    },

    {
        "kategori": "Ejaan kata ulang",
        "tanya": "Penulisan kata ulang yang benar adalah ...",
        "pilihan": [
            "anak-anak, kura-kura, sayur-mayur",
            "anakanak, kurakura, sayurmayur",
            "anak-anak, kura kura, sayur mayur",
            "anak2, kura-kura, sayur mayur",
        ],
        "benar": 0,
        "penjelasan": "Kata ulang ditulis dengan tanda hubung, termasuk kata ulang berubah bunyi seperti sayur-mayur. Penulisan tanpa tanda hubung (anakanak) atau dengan angka (anak2) tidak dipakai dalam tulisan resmi.",
        "hint": [
            "Cek satu hal saja: tanda hubung pada kata ulang.",
            "Kata ulang ditulis dengan tanda hubung tanpa spasi: anak-anak, kura-kura.",
            "Ada pilihan yang tanda hubungnya lengkap, tetapi memakai bentuk anak2. Buang yang itu.",
        ],
    },

    {
        "kategori": "Surel resmi",
        "tanya": "Kamu ingin meminta Bu Rina menjadi pembina Klub Bahasa di sekolah. Pilih isi surel yang paling tepat.",
        "pilihan": [
            "Yth. Ibu Rina, kami mohon kesediaan Ibu untuk menjadi pembina Klub Bahasa. Atas perhatian Ibu, kami ucapkan terima kasih.",
            "Yth. Bu Rina, kami mau Ibu jadi pembina klub kami. Makasih ya Bu.",
            "Yth. Ibu Rina, kami mohon Ibu jadi pembina Klub Bahasa. Kami tunggu ya Bu.",
            "Halo Bu Rina, tolong banget ya jadi pembina klub bahasa. Kami tunggu lho.",
        ],
        "benar": 0,
        "penjelasan": "Surel resmi memerlukan sapaan hormat (Yth. Ibu ...), kata baku (menjadi, bukan jadi), kata santun seperti mohon kesediaan, serta penutup berupa ucapan terima kasih. Pilihan lain masih memakai ragam santai (mau, makasih, ya) atau terkesan menekan pembaca.",
        "hint": [
            "Surel resmi punya empat bagian: sapaan hormat, isi permohonan yang jelas, kata baku, dan penutup.",
            "Periksa kata bakunya: 'jadi' seharusnya 'menjadi', 'mau' seharusnya 'mohon', 'makasih' seharusnya 'terima kasih'.",
            "Dua pilihan sudah memakai Yth. Ibu Rina. Buang yang masih memakai kata jadi atau terkesan menekan pembaca.",
        ],
    },
]


# ---------------------------------------------------------------------------
# CHAPTER
# ---------------------------------------------------------------------------

label chapter_indonesia:

    $ teks = TEKS_ID
    $ putar_musik("bgm_kuis.ogg")

    scene bg kelas sore with fade
    show char hina senyum-buka at kanan

    "Kelas sore. Cahaya dari jendela bergerak pelan di atas meja."
    "Kelas elektif bahasa Indonesia. Cuma lima orang."
    "Bu Rina Hartati, guru pertukaran dari Jakarta, katanya menilai kami dengan standar yang sama seperti di sekolahnya."
    "Jujur, aku tidak terlalu bersemangat."

    h "[nama_mc], kamu ikut kelas tambahan, kan?"
    r "Iya. Kamu kenapa masih di sini?"
    h "Penasaran. Katanya Bu Rina galak."
    r "Jangan bikin aku makin takut."

    show char hina senyum-mata at kanan with dissolve

    h "Santai. Aku cuma nonton."

    "Hina duduk di kursi sebelah, membuka buku catatannya."

    show char hina fokus at kanan with dissolve

    h "Tapi sebelum mulai, aku mau kasih aturan main."
    r "Kamu bukan gurunya."
    h "Justru karena bukan guru, aku bisa jujur."
    h "Aturannya cuma satu: jangan cuma nebak. Kamu harus bisa jelasin alasannya."
    h "Petunjuk cuma boleh sekali per soal. Makin tajam petunjuknya, makin besar potongan kemandirianmu."
    r "Kemandirian?"
    h "Nilai akhir itu 70 persen benar, 30 persen mandiri. Jadi kalau semua jawaban benar tapi kamu nyaris nggak mikir, tetap nggak bisa dapat A."
    r "Ketat juga."
    h "Dua soal pertama pemanasan. Petunjuknya gratis."
    h "Sisanya, kamu yang pilih: mau minta arahan, strategi, atau hampir jawaban."
    r "Kayak beli petunjuk di game."

    show char hina tertawa at kanan with dissolve

    h "Bedanya, ini hidupmu."
    r "……itu tadi berlebihan."
    h "Sedikit. Sekarang mulai."

    # Pemanasan dari guru, bukan dari Hina (khas rute Indonesia).
    show char rina netral at kiri with dissolve

    rina "Sebelum soal pertama, satu pertanyaan dari saya."
    rina "Mana yang baku: 'nggak' atau 'tidak'?"
    r "……'Tidak', Bu."
    rina "Kenapa?"
    r "Karena 'nggak' cuma bahasa lisan. Di tulisan resmi, kata bakunya 'tidak'."

    show char rina puas at kiri with dissolve

    rina "Bagus. Saya tidak menilai hafalan. Saya menilai kamu tahu alasannya."
    "（Bu Rina kembali ke mejanya. Batik di lengannya masih terlipat rapi.）"

    show char hina netral at kanan with dissolve

    h "……Jawaban itu dari dia, bukan dari aku."

    # Beat 1 — pemanasan (2 soal, hint gratis)
    "Dua soal pertama memang terasa lebih ringan. Hina tidak banyak bicara, hanya sesekali mengetuk meja."

    call satu_soal(SOAL_ID, 0, teks)
    call satu_soal(SOAL_ID, 1, teks)

    # Beat 2 — koridor
    call interlude_koridor

    # Beat 3 — tantangan (4 soal, hint berbayar)
    scene bg kelas sore with fade
    show char hina netral at kanan

    "Kami kembali ke kelas. Kursi-kursi lain sudah kosong sejak tadi."

    h "Aturan tadi berlaku penuh mulai sekarang."
    r "Kalau aku salah pilih?"

    show char hina senyum-mata at kanan with dissolve

    h "Ya tinggal dijelaskan. Salah itu bukan akhir."

    call satu_soal(SOAL_ID, 2, teks)
    call satu_soal(SOAL_ID, 3, teks)
    call satu_soal(SOAL_ID, 4, teks)
    call satu_soal(SOAL_ID, 5, teks)

    # Beat 4 — kantin
    call interlude_kantin

    # Beat 5 — klimaks (2 soal)
    call interlude_malam

    "（Aku menarik napas. Dua soal terakhir. Tidak ada lagi waktu untuk ragu.）"

    call satu_soal(SOAL_ID, 6, teks)
    call satu_soal(SOAL_ID, 7, teks)

    # Beat 6 — hening sebelum nilai keluar: musik berhenti, tidak ada dialog dulu.
    stop music fadeout 2.0

    "Aku menutup jawaban soal terakhir. Ruang elektif yang tadi diisi lima orang sekarang tinggal kami."
    "Bu Rina merapikan buku nilainya pelan-pelan, seperti sengaja memberi waktu."
    "Hina menyeruput air dari botolnya, lalu menutup botol itu tanpa suara."

    show char hina netral at kanan with dissolve

    h "……"
    h "Nilainya cuma angka. Yang kamu ngerti, itu yang kamu bawa pulang."

    jump penilaian
