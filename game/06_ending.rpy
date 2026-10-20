# ===========================================================================
# 06_ending.rpy  —  PENILAIAN & ENDING
# ===========================================================================
#  A : nilai >= 85
#  B : 65 <= nilai < 85
#  C : nilai < 65
#
#  Kedua mapel memakai dialog/UI bahasa Indonesia. Yang berbeda hanya guru
#  dan materi soalnya. Setelah ending:
#      [Coba mapel lain] -> pemilihan mapel
#      [Keluar]          -> menu utama
# ===========================================================================


label penilaian:

    # Hindari quick menu menutupi tombol rapor/ending.
    $ quick_menu = False

    $ total_soal = 8
    $ nilai = hitung_nilai(benar, total_soal, mandiri)
    $ huruf = huruf_nilai(nilai)

    # Musik rapor + ending mengikuti huruf nilai (A/B/C).
    $ putar_musik("bgm_akhir_%s.ogg" % huruf.lower())

    scene bg kelas malam with fade
    hide char

    if mapel_aktif == "ja":

        if huruf == "A":
            show char sakuraba puas at kiri
            sk "……Bagus, [nama_mc]. Kamu tidak hanya menebak."
            r "Maaf, Sensei?"
            sk "Kamu bisa menjelaskan alasan jawabanmu. Itu yang paling penting."
            "（Sakuraba-sensei mengangguk pelan.）"
            sk "Pertahankan di kelas berikutnya."

        elif huruf == "B":
            show char sakuraba netral at kiri
            sk "……Cukup. Lulus."
            r "Cukup, Sensei?"
            sk "Tidak buruk. Tapi beberapa jawabanmu masih lemah alasannya."
            sk "Kalau jawabannya benar tapi tidak bisa dijelaskan, itu belum jadi kemampuanmu."
            r "……Saya mengerti."
            sk "Kita perbaiki bagian itu lain kali."

        else:
            show char sakuraba tegas at kiri
            sk "……[nama_mc]."
            r "Iya, Sensei."
            sk "Hasilnya belum memuaskan. Tapi aku tidak melihat kamu belajar sia-sia hari ini."
            sk "Yang kurang adalah latihan. Besok kita mulai lagi dari dasar."

    else:

        if huruf == "A":
            show char rina puas at kiri
            rina "……Baik. [nama_mc], kamu paham."
            r "Maaf, Bu?"
            rina "Bukan cuma jawabannya. Cara kamu memilih jawaban juga. Itu yang saya nilai."
            "（Bu Rina menutup buku nilai dan tersenyum tipis.）"
            rina "Pertahankan. Kelas berikutnya jangan kendor."

        elif huruf == "B":
            show char rina netral at kiri
            rina "Nilaimu aman. Lulus, tapi belum matang."
            r "Belum matang?"
            rina "Ada beberapa jawaban yang benar, tapi alasannya belum kuat."
            rina "Kalau kamu tidak bisa menjelaskan, itu belum jadi milikmu."
            r "……Saya mengerti."
            rina "Bagus. Kita perbaiki bagian itu."

        else:
            show char rina tegas at kiri
            rina "[nama_mc]."
            r "Iya, Bu."
            rina "Saya tidak akan berbasa-basi. Hasilmu belum cukup."
            rina "Tapi saya lihat kamu berusaha. Itu bukan nol."
            rina "Besok, kita mulai lagi dari dasar. Satu per satu."

    call screen rapor(teks)

    if huruf == "A":
        jump ending_a
    elif huruf == "B":
        jump ending_b
    else:
        jump ending_c


# ---------------------------------------------------------------------------
# ENDING A
# ---------------------------------------------------------------------------

label ending_a:

    $ persistent.akhir_a = True

    scene bg kelas malam with fade
    show char hina senyum at kanan

    "Udara kelas mereda. Suara detak jam dinding terasa lebih pelan."

    show char hina senyum-mata at kanan with dissolve

    h "……Syukurlah. Beneran."
    r "Berkat kamu."

    show char hina senyum-buka at kanan with dissolve

    h "Nggak. Yang milih jawaban terakhir itu kamu."
    "（Hina menutup buku catatannya, lalu melihat ke luar jendela.）"
    h "Kata-kata itu bukan cuma buat dihafal. Dia dipilih."
    r "……Hari ini aku mulai ngerti."

    show char hina tertawa at kanan with dissolve

    h "Iya. Muka kamu bilang gitu."
    "（Lampu kelas terasa sedikit lebih hangat dari tadi.）"

    show char hina senyum-mata at kanan with dissolve

    h "Ayo, pulang."
    r "Rumah kamu ke arah sebaliknya."
    h "Mau mampir dulu."
    r "Mampir di mana?"
    h "Pokoknya ikut."
    "（Dia jalan duluan. Langkahnya pelan—jauh lebih pelan dari biasanya.）"
    "（Di ujung koridor, dia menoleh sebentar. Memastikan aku masih di belakang.）"

    call screen akhir_mapel(teks)

    if _return == "ulang":
        jump pilih_mapel
    return


# ---------------------------------------------------------------------------
# ENDING B
# ---------------------------------------------------------------------------

label ending_b:

    $ persistent.akhir_b = True

    scene bg kelas malam with fade
    show char hina netral at kanan

    h "……Yah, lulus."
    r "Lega?"
    h "Sedikit. Tapi tadi beberapa jawabanmu cuma tebakan, kan?"
    r "……Ketahuan?"
    h "Jelas."
    "（Hina menarik bukuku dan menandai halaman yang salah.）"
    h "Bagian ini, lain kali alasanmu harus bisa dijelaskan."
    r "Iya, Bu."
    h "Aku bukan Bu. ……Tapi ya udah."

    show char hina senyum-mata at kanan with dissolve

    h "Sisanya, aku yang bantu selesaikan. Kamu nggak harus nanggung sendiri."
    r "Kenapa repot-repot?"
    h "……Karena kamu nanya."
    "（Dia mengetuk meja dua kali, lalu berdiri. Tasnya sudah di pundak, tapi dia belum pergi.）"
    h "Besok, jam empat. Di sini."
    r "Kalau aku telat?"
    h "Aku tunggu sepuluh menit."
    r "Terus?"
    h "Terus aku mulai tanpa kamu. Kamu nyusul sendiri."
    "（Aku belum bisa memastikan apakah itu ancaman.）"

    call screen akhir_mapel(teks)

    if _return == "ulang":
        jump pilih_mapel
    return


# ---------------------------------------------------------------------------
# ENDING C
# ---------------------------------------------------------------------------

label ending_c:

    $ persistent.akhir_c = True

    scene bg kelas malam with fade
    show char hina kecewa at kanan

    "Lampu kelas terasa lebih putih dari biasanya."
    h "……[nama_mc]. Nggak apa-apa."
    r "Ini jelas nggak apa-apa."
    h "Iya. Tapi ini belum akhir."
    r "……"
    h "Besok kita ulang dari awal. Tanpa petunjuk. Satu per satu."
    r "Kamu mau bantuin lagi?"

    show char hina senyum-mata at kanan with dissolve

    h "Ya iyalah."
    r "Bahkan setelah aku gagal?"
    h "Gagal apa? Baru satu malam."
    "（Dia mengangkat tasnya, lalu berhenti di pintu kelas.）"
    h "Aku tunggu di gerbang. Lima menit."
    r "Kalau aku lama?"
    h "Ya aku tunggu lebih lama. Jangan bikin aku ngomong dua kali."
    "（Aku tidak tahu harus menjawab apa. Tapi Hina tidak menunggu jawaban.）"

    call screen akhir_mapel(teks)

    if _return == "ulang":
        jump pilih_mapel
    return
