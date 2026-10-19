# ===========================================================================
# 04_bahasa_jepang.rpy  —  CHAPTER BAHASA JEPANG
# ===========================================================================
#  Mapel ini tetap berisi materi bahasa Jepang, tetapi:
#    - semua narasi, dialog Hina, dialog guru, dan UI memakai bahasa Indonesia
#    - soal ditulis dalam hiragana/katakana saja (tanpa kanji)
#      + romaji + arti bahasa Indonesia
#    - pilihan jawaban juga memakai huruf Jepang + romaji + arti
#    - penjelasan dan hint memakai bahasa Indonesia
#
#  Tujuannya: pemain yang belum bisa membaca kanji tetap bisa mengerjakan soal.
# ===========================================================================


# ---------------------------------------------------------------------------
# BANK SOAL — 8 SOAL
# ---------------------------------------------------------------------------

define SOAL_JA = [

    {
        "kategori": "Partikel",
        "tanya": "Isi bagian kosong dengan partikel yang tepat.\nわたしは まいにち にほんご（　）べんきょうします。\nWatashi wa mainichi nihongo ( ) benkyou shimasu.\nArti: Saya belajar bahasa Jepang setiap hari.",
        "pilihan": [
            "を (o)\nPenanda objek",
            "が (ga)\nPenanda subjek",
            "に (ni)\nPenanda waktu/tujuan",
            "で (de)\nPenanda tempat/alat",
        ],
        "benar": 0,
        "penjelasan": "Kata kerja べんきょうします (benkyou shimasu) adalah kata kerja transitif yang membutuhkan objek. Objek ditandai partikel を (o). Partikel が (ga) menandai subjek, に (ni) menandai waktu/tujuan, dan で (de) menandai tempat atau alat.",
        "hint": [
            "Lihat kata kerjanya: べんきょうします (benkyou shimasu). Kata kerja ini butuh objek.",
            "Partikel untuk objek adalah を (o). Partikel が (ga) dipakai untuk subjek.",
            "Pilih antara を (o) dan に (ni). にほんご (nihongo) adalah hal yang dipelajari, jadi dia objek.",
        ],
    },

    {
        "kategori": "Katakana",
        "tanya": "Pilih kata yang berarti 'toko serba ada yang buka 24 jam'.",
        "pilihan": [
            "コンビニ (konbini)\nToko serba ada 24 jam",
            "レストラン (resutoran)\nRestoran",
            "スーパー (suupaa)\nSupermarket",
            "デパート (depaato)\nDepartment store",
        ],
        "benar": 0,
        "penjelasan": "コンビニ (konbini) adalah singkatan dari convenience store, yaitu toko serba ada yang buka 24 jam. レストラン (resutoran) = restoran, スーパー (suupaa) = supermarket, デパート (depaato) = department store.",
        "hint": [
            "Kata ini sering muncul di jalan dan biasanya buka 24 jam.",
            "Bentuknya katakana, dan artinya 'toko serba ada'.",
            "Pilihan yang benar diawali コン (kon), bukan レス (resu) atau スー (suu).",
        ],
    },

    {
        "kategori": "Gaya bahasa tulis",
        "tanya": "Kalimat mana yang paling tepat untuk laporan tertulis?\n(Gunakan gaya だ・である / da de aru, bukan gaya percakapan.)",
        "pilihan": [
            "じっけんの けっか、みずの おんどは あがった。\nJikken no kekka, mizu no ondo wa agatta.\nHasil percobaan: suhu air naik. (gaya だ・である)",
            "じっけんの けっか、みずの おんどは あがりました。\nJikken no kekka, mizu no ondo wa agarimashita.\nHasil percobaan: suhu air naik. (gaya です・ます)",
            "じっけんの けっか、みずの おんどは あがるよね。\nJikken no kekka, mizu no ondo wa agaru yo ne.\nHasil percobaan: suhu air naik. (gaya percakapan, よね)",
            "じっけんの けっか、みずの おんどは あがっちゃった。\nJikken no kekka, mizu no ondo wa agacchatta.\nHasil percobaan: suhu air naik. (gaya percakapan santai, ちゃった)",
        ],
        "benar": 0,
        "penjelasan": "Laporan tertulis memakai gaya だ・である (da/de aru), bukan です・ます (desu/masu) yang ditujukan kepada lawan bicara. Bentuk あがるよね (agaru yo ne) dan あがっちゃった (agacchatta) adalah bahasa percakapan.",
        "hint": [
            "Laporan tertulis bukan percakapan. Pilih gaya だ・である.",
            "です・ます (desu/masu) adalah gaya sopan untuk berbicara. よね dan ちゃった adalah ciri percakapan.",
            "Cari kalimat yang berakhir dengan あがった (agatta), bukan あがりました (agarimashita).",
        ],
    },

    {
        "kategori": "Keigo (bahasa hormat)",
        "tanya": "Pasangan mana yang benar?\nそんけいご (sonkeigo) = bentuk hormat untuk tindakan orang lain.\nけんじょうご (kenjougo) = bentuk rendah diri untuk tindakan sendiri.",
        "pilihan": [
            "おっしゃる (ossharu — sonkeigo 'berkata')\nもうす (mousu — kenjougo 'berkata')",
            "いたす (itasu — sonkeigo)\nなさる (nasaru — kenjougo)",
            "ごらんになる (goran ni naru — kenjougo)\nはいけんする (haiken suru — sonkeigo)",
            "いらっしゃる (irassharu — kenjougo)\nうかがう (ukagau — sonkeigo)",
        ],
        "benar": 0,
        "penjelasan": "Sonkeigo dipakai untuk tindakan orang lain atau atasan; kenjougo untuk tindakan sendiri. おっしゃる (ossharu), なさる (nasaru), ごらんになる (goran ni naru), dan いらっしゃる (irassharu) adalah sonkeigo. もうす (mousu), いたす (itasu), はいけんする (haiken suru), dan うかがう (ukagau) adalah kenjougo. Pilihan lain membalik jenisnya.",
        "hint": [
            "Ingat: sonkeigo untuk tindakan orang lain, kenjougo untuk tindakan sendiri.",
            "もうす (mousu), いたす (itasu), はいけんする (haiken suru), dan うかがう (ukagau) semuanya kenjougo.",
            "おっしゃる (ossharu) dan もうす (mousu) sama-sama berarti 'berkata'. Mana yang untuk orang lain?",
        ],
    },

    {
        "kategori": "Pola kalimat",
        "tanya": "Kalimat mana yang menunjukkan keputusan sendiri?\n(Pilih yang memakai pola 〜ことにする / koto ni suru.)",
        "pilihan": [
            "らいねん、にほんへ りゅうがくする ことにした。\nRainen, nihon e ryuugaku suru koto ni shita.\nTahun depan saya memutuskan belajar ke Jepang.",
            "らいねん、にほんへ りゅうがくする ように なった。\nRainen, nihon e ryuugaku suru you ni natta.\nTahun depan saya jadi bisa/perlu belajar ke Jepang. (perubahan)",
            "らいねん、にほんへ りゅうがくする ことに なった。\nRainen, nihon e ryuugaku suru koto ni natta.\nTahun depan diputuskan bahwa saya akan belajar ke Jepang. (keputusan pihak lain)",
            "らいねん、にほんへ りゅうがくする ように した。\nRainen, nihon e ryuugaku suru you ni shita.\nTahun depan saya berusaha agar bisa belajar ke Jepang. (usaha)",
        ],
        "benar": 0,
        "penjelasan": "〜ことにする (koto ni suru) = memutuskan sendiri. 〜ことになる (koto ni naru) = diputuskan oleh pihak lain/keadaan. 〜ようになる (you ni naru) = perubahan kemampuan/kebiasaan. 〜ようにする (you ni suru) = berusaha/berhati-hati agar terjadi.",
        "hint": [
            "Bedakan する (suru) dan なる (naru). Keputusan sendiri memakai する.",
            "〜ことにした (koto ni shita) = sudah memutuskan sendiri. 〜ことになった (koto ni natta) = keputusan dari luar.",
            "Antara ことにした (koto ni shita) dan ようにした (you ni shita). Yang pertama keputusan, yang kedua usaha.",
        ],
    },

    {
        "kategori": "Kosakata",
        "tanya": "Pilih kata yang berarti 'lancar, berjalan sesuai rencana'.",
        "pilihan": [
            "じゅんちょう (junchou)\nLancar, sesuai rencana",
            "ふちょう (fuchou)\nTidak lancar, macet",
            "けいかく (keikaku)\nRencana",
            "しごと (shigoto)\nPekerjaan",
        ],
        "benar": 0,
        "penjelasan": "じゅんちょう (junchou) berarti lancar atau berjalan sesuai rencana. ふちょう (fuchou) adalah kebalikannya, yaitu tidak lancar. けいかく (keikaku) = rencana, しごと (shigoto) = pekerjaan.",
        "hint": [
            "Kata ini sering dipakai untuk pekerjaan atau rencana yang berjalan baik.",
            "Artinya 'lancar'. Lawannya ふちょう (fuchou).",
            "Pilih じゅんちょう (junchou), bukan ふちょう (fuchou).",
        ],
    },

    {
        "kategori": "Pemahaman bacaan",
        "tanya": "きのう、ともだちに「あしたは はやく こい」と いわれた。\nKinou, tomodachi ni \"ashita wa hayaku koi\" to iwareta.\nArti: Kemarin saya dikatakan oleh teman, \"Besok datang lebih awal.\"\nSiapa yang menerima tindakan いわれた (iwareta — dikatakan)?",
        "pilihan": [
            "わたし (watashi — saya)",
            "ともだち (tomodachi — teman)",
            "ともだちと わたし (tomodachi to watashi — teman dan saya)",
            "きめられない (kimerarenai — tidak bisa ditentukan)",
        ],
        "benar": 0,
        "penjelasan": "〜に いわれた (ni iwareta) adalah bentuk pasif. Tindakan 'berkata' dilakukan oleh ともだち (tomodachi), dan yang menerima tindakan adalah わたし (watashi) — subjek kalimat. Dalam bahasa Jepang, subjek sering dihilangkan.",
        "hint": [
            "いわれた (iwareta) adalah bentuk pasif dari いう (iu — berkata). Subjeknya adalah yang menerima tindakan.",
            "Partikel に pada ともだちに (tomodachi ni) menunjukkan pelaku yang melakukan tindakan.",
            "Yang berkata adalah teman. Yang dikatakan adalah...?",
        ],
    },

    {
        "kategori": "Email formal",
        "tanya": "Sakuraba-sensei mengirim email:\n「あしたの ほしゅう、しりょうを まとめておいてくれると たすかります。」\nAshita no hoshuu, shiryou o matomete oite kureru to tasukarimasu.\nArti: Untuk kelas tambahan besok, kalau kamu mau merangkum materinya, saya akan terbantu.\nPilih balasan yang paling tepat.",
        "pilihan": [
            "かしこまりました。あしたまでに しりょうを まとめておきます。よろしく おねがいいたします。\nKashikomarimashita. Ashita made ni shiryou o matomete okimasu. Yoroshiku onegai itashimasu.\nBaik, saya mengerti. Saya akan merangkum materinya sampai besok. Terima kasih.",
            "りょうかいです！まとめときますねー。\nRyoukai desu! Matomete okimasu nee.\nSiap! Aku rangkum ya. (santai)",
            "しりょうを まとめておいてくれるんですね。ありがとうございます！\nShiryou o matomete oite kureru n desu ne. Arigatou gozaimasu!\nJadi kamu yang merangkumnya, ya. Terima kasih! (salah arah)",
            "あしたは よていが あるので、たぶん むりだと おもいます。\nAshita wa yotei ga aru node, tabun muri da to omoimasu.\nBesok saya ada acara, sepertinya tidak bisa. (menolak tanpa solusi)",
        ],
        "benar": 0,
        "penjelasan": "Email kepada guru memerlukan keigo. かしこまりました (kashikomarimashita) adalah bentuk hormat untuk 'mengerti/menerima'. 〜ておきます (te okimasu) menunjukkan persiapan. よろしく おねがいいたします (yoroshiku onegai itashimasu) adalah penutup sopan. Pilihan 2 memakai bahasa santai (りょうかい, ねー), pilihan 3 salah memahami permintaan, pilihan 4 menolak tanpa solusi.",
        "hint": [
            "Pengirimnya guru. Balasan harus memakai keigo, bukan bahasa santai.",
            "りょうかいです (ryoukai desu) dan ねー (nee) terlalu santai untuk guru. Gunakan かしこまりました (kashikomarimashita).",
            "Pilih balasan yang menerima permintaan dan menyebutkan kapan materi akan selesai.",
        ],
    },
]


# ---------------------------------------------------------------------------
# CHAPTER
# ---------------------------------------------------------------------------

label chapter_jepang:

    $ teks = TEKS_ID

    scene bg kelas sore with fade
    show char hina senyum-buka at kanan

    "Kelas sore. Di luar, langit sudah mulai berwarna jingga."
    "Hari ini ada kelas tambahan bahasa Jepang bersama Sakuraba-sensei. Jujur, aku belum terlalu siap."
    "Sakuraba-sensei bilang, untuk kelas pertukaran, penjelasan boleh memakai bahasa Indonesia. Soalnya tetap bahasa Jepang, tapi setiap soal diberi romaji dan arti."

    h "Rei, kamu ikut kelas tambahan, kan?"
    r "Iya. Kamu kenapa masih di sini?"
    h "Penasaran. Katanya Sakuraba-sensei galak kalau soal partikel."
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
    h "Soalnya pakai hiragana dan katakana, tapi aku sudah siapkan romaji dan artinya. Jadi kamu bisa fokus ke bacaan dan artinya dulu."
    r "Bagus. Aku hampir panik tadi."
    h "Jangan panik. Baca pelan-pelan. Sekarang mulai."

    "Dua soal pertama memang terasa lebih ringan. Hina tidak banyak bicara, hanya sesekali mengetuk meja."

    call satu_soal(SOAL_JA, 0, teks)
    call satu_soal(SOAL_JA, 1, teks)

    call interlude_koridor

    scene bg kelas sore with fade
    show char hina netral at kanan

    "Kami kembali ke kelas. Kursi-kursi lain sudah kosong sejak tadi."

    h "Mulai dari sini, tiap petunjuk ada harganya. Pilih dengan sadar."
    r "Kalau aku salah pilih?"

    show char hina senyum-mata at kanan with dissolve

    h "Ya tinggal dijelaskan. Salah itu bukan akhir."
    h "Untuk soal Jepang, baca dulu kalimat Jepangnya, lalu romaji, lalu artinya. Jangan keburu lihat pilihan."
    r "Oke. Pelan-pelan."

    call satu_soal(SOAL_JA, 2, teks)
    call satu_soal(SOAL_JA, 3, teks)
    call satu_soal(SOAL_JA, 4, teks)
    call satu_soal(SOAL_JA, 5, teks)

    call interlude_kantin

    call interlude_malam

    r "（Aku menarik napas. Dua soal terakhir. Tidak ada lagi waktu untuk ragu.)"

    call satu_soal(SOAL_JA, 6, teks)
    call satu_soal(SOAL_JA, 7, teks)

    jump penilaian
