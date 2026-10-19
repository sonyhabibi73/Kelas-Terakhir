# ===========================================================================
# 03_hina.rpy  —  HINA
# ===========================================================================
#  Hina bukan oracle. Ia hanya memberi tiga jenis bantuan:
#      level 0  arahan   (10)  — membaca ulang soal dengan kata lain
#      level 1  strategi (20)  — memberi aturan/rumus, bukan jawaban
#      level 2  hampir   (35)  — mempersempit ke dua pilihan
#
#  Satu soal hanya boleh memakai satu petunjuk. Dua soal pemanasan gratis.
#  Semua dialog Hina berbahasa Indonesia, termasuk di mapel Bahasa Jepang.
# ===========================================================================


label hina_hint(level, soal, gratis):

    $ biaya = biaya_hint(level, gratis)
    $ mandiri = max(0, mandiri - biaya)

    show char hina fokus at kanan

    $ pesan_hint = soal["hint"][level]
    h "[pesan_hint]"

    return


# ---------------------------------------------------------------------------
# INTERLUDE 1 — KORIDOR
# ---------------------------------------------------------------------------

label interlude_koridor:

    scene bg koridor with fade
    show char hina netral at kanan

    "Koridor sekolah sudah sepi. Yang tersisa cuma suara lampu neon dan langkah kami."
    h "Jeda pertama. Gimana? Pemanasan tadi aman?"
    r "Aman karena petunjuknya gratis."
    h "Berarti kamu sadar. Bagus."
    h "Mulai sekarang, tiap petunjuk ada harganya. Arahan 10, strategi 20, hampir jawaban 35."
    r "Yang 35 itu praktis jawabannya, ya?"
    h "Bukan. Itu cuma mempersempit pilihan. Jawaban akhirnya tetap kamu yang pilih."
    h "Dan ingat: satu soal, satu petunjuk. Nggak bisa dicicil."
    r "Jadi harus milih dengan sadar."
    h "Iya. Itu intinya."

    return


# ---------------------------------------------------------------------------
# INTERLUDE 2 — KANTIN
# ---------------------------------------------------------------------------

label interlude_kantin:

    scene bg kantin with fade
    show char hina senyum at kanan

    "Kantin hampir kosong. Wangi kayu meja bercampur bau makanan yang sudah dingin."
    h "Tadi pas salah, kamu kesel?"
    r "Sedikit."
    h "Cuma sedikit?"
    r "Ya. Karena aku tahu kenapa aku salah."
    h "Nah. Itu bagus."
    r "Masa salah itu bagus?"
    h "Bukan salahnya. Tapi kamu tahu alasannya. Itu bedanya sama orang yang benar karena untung."
    h "Kalau kamu cuma nebak dan kebetulan benar, besok kamu bakal salah lagi."
    h "Jadi, mending salah tapi alasannya jelas, daripada benar tapi nggak tahu kenapa."
    r "Itu agak menghibur."
    h "Dua soal terakhir berat. Tapi kamu udah punya bekal. Jangan buru-buru."

    return


# ---------------------------------------------------------------------------
# INTERLUDE 3 — KELAS MALAM
# ---------------------------------------------------------------------------

label interlude_malam:

    scene bg kelas malam with fade
    show char hina fokus at kanan

    "Di luar sudah gelap. Lampu kelas terasa lebih putih dari tadi."
    h "Dua soal terakhir. Ini bagian yang paling nggak bisa ditawar."
    r "Aku tahu."
    h "Petunjuk cuma satu. Setelah itu, kamu sendiri."
    r "……Oke."
    h "Jangan lihat aku terus. Lihat soalnya."
    r "（Hina menyandarkan punggung ke kursi, memberi ruang.)"

    return
