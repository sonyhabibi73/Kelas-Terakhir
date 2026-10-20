# ===========================================================================
# 01_prolog.rpy  —  PROLOG CERITA
# ===========================================================================
#  Urutan:
#    rumah Rei  ->  pamitan dengan Ibu
#    koridor    ->  Rei nabrak Hina, lalu Hina menarik tangannya
#    kelas      ->  perkenalan singkat, lalu Hina menawarkan kelas tambahan
#
#  Setelah prolog, pemain masuk ke layar "Pilih kelas tambahan"
#  (label pilih_mapel di 01_config.rpy).
# ===========================================================================


label prolog:

    $ quick_menu = True
    $ putar_musik("bgm_hari.ogg")

    # -----------------------------------------------------------------------
    # RUMAH REI — PAGI
    # -----------------------------------------------------------------------

    scene bg rumah with fade
    show char ibu senyum at kiri

    "Pagi itu, rumah terasa lebih hangat dari biasanya."
    "Aku berdiri di depan pintu, merapikan seragam baru. Hari ini hari pertamaku di sekolah ini."
    "Aku sudah memeriksa tas tiga kali: buku, dompet, dan botol minum. Semuanya ada."

    ibu "[nama_mc], kelas tambahannya mulai hari ini, ya?"
    r "Iya. Dua minggu lagi program pertukarannya selesai."
    ibu "Jadi ini kesempatan terakhir kamu belajar sama guru-guru itu."
    r "……Iya, Bu."
    ibu "Ibu nggak minta nilai kamu bagus."
    ibu "Ibu cuma mau kamu ngerti apa yang kamu pelajari."
    r "Aku tahu."

    ibu "[nama_mc], sarapan dulu. Jangan sampai telat di hari pertama."
    r "Iya, Bu. Aku sudah makan."
    ibu "Jangan lupa bawa buku dan dompet. Kalau ada apa-apa, telepon Ibu."
    r "Iya. Aku berangkat."
    ibu "Hati-hati di jalan."

    "Ibu melambaikan tangan sampai aku menghilang di tikungan."
    "Dua minggu. Setelah itu para guru pertukaran pulang, dan kelas tambahan ini selesai."
    "Aku menarik napas panjang. Sekolah baru, wajah-wajah baru. Semoga semuanya berjalan lancar."


    # -----------------------------------------------------------------------
    # KORIDOR SEKOLAH — NABRAK HINA
    # -----------------------------------------------------------------------

    scene bg koridor with fade

    "Sekolah baruku lebih besar dari bayanganku. Koridornya panjang, lokernya biru, dan baunya masih seperti cat baru."
    "Aku mempercepat langkah. Kata orang, bel masuk di sekolah ini sangat tepat waktu."

    show char hina kaget at kanan

    "Saat aku belok di sudut koridor, seseorang menabrakku."

    h "Aduh!"
    r "Maaf! Aku tidak lihat—"

    show char hina netral at kanan with dissolve

    h "Kamu murid baru ya?"
    r "Iya."
    h "Kelas berapa kamu?"
    r "Kelas 11 IPA 2."

    show char hina senyum at kanan with dissolve

    h "Kita sekelas. Ayo ikut aku, kita udah mau telat."

    "Hina menarik tanganku sebelum aku sempat bertanya."
    "Tangannya hangat. Aku hanya bisa mengikuti langkahnya, setengah berlari melewati koridor."


    # -----------------------------------------------------------------------
    # KELAS 11 IPA 2
    # -----------------------------------------------------------------------

    scene bg kelas sore with fade
    show char hina senyum-buka at kanan

    "Kami sampai di kelas tepat saat bel berbunyi."

    h "Selamat datang di kelas 11 IPA 2. Aku Hina."
    r "Rei. Terima kasih sudah menunjukkan jalan."

    show char hina senyum-mata at kanan with dissolve

    h "Sama-sama. Nanti kalau ada yang bingung, tanya aku saja."

    "Hari pertama berjalan lebih cepat dari yang aku bayangkan."
    "Hina banyak membantuku: menunjukkan loker, menjelaskan jadwal, dan memperkenalkanku ke beberapa teman sekelas."

    show char hina netral at kanan with dissolve

    "Saat pelajaran terakhir selesai, Hina menoleh ke arahku."

    h "Oh iya, hari ini ada kelas tambahan. Kamu mau ikut yang mana?"
    r "Kelas tambahan?"
    h "Iya. Ada kelas bahasa Jepang dan kelas bahasa Indonesia. Dua-duanya lumayan menantang."
    h "Program pertukarannya selesai dua minggu lagi. Yang nilainya bagus bisa ikut kelas tingkat lanjut."
    r "Kamu ikut?"
    h "Ikut. Aku juga perlu lanjut."
    r "Aku belum tahu harus pilih yang mana."
    h "Ya pilih yang kamu mau. Aku ikut kamu."

    "Hina menatapku sambil menunggu jawaban."
    "Aku melihat papan tulis, lalu ke luar jendela. Kelas sore ini masih panjang."

    jump pilih_mapel
