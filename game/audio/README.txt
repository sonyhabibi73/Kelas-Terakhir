MUSIK & EFEK SUARA — 「最後の授業」/ Kelas Terakhir
=================================================

Musik (bgm_*.ogg)
-----------------
Semua lagu dari koleksi Musopen "The Complete Chopin Collection", pemain
Aaron Dunn. Karya Chopin sudah menjadi domain publik, dan rekamannya
dilepas dengan lisensi CC0 (public domain dedication) — bebas dipakai,
diubah, dan dibagikan, termasuk untuk tugas sekolah.

  Sumber : https://archive.org/details/musopen-chopin
  Lisensi: CC0 1.0 — https://creativecommons.org/publicdomain/zero/1.0/

  bgm_menu.ogg      Nocturne Op. 9 no. 2 in E flat major
  bgm_hari.ogg      Mazurka Op. 50 no. 1 in G major
  bgm_kuis.ogg      Prelude Op. 28 no. 12
  bgm_akhir_a.ogg   Waltz Op. 69 no. 1 in A flat major
  bgm_akhir_b.ogg   Prelude Op. 28 no. 6 in B minor
  bgm_akhir_c.ogg   Mazurka Op. 17 no. 4 in A minor

Dipakai di mana (lihat 07_audio.rpy, dan tiap label cerita):
  menu       -> layar judul + layar pilih kelas tambahan
  hari       -> prolog + interlude koridor/kantin/kelas malam
  kuis       -> chapter Jepang & Indonesia
  akhir_x    -> rapor + ending sesuai huruf nilai (A/B/C)

Efek suara (wav)
----------------
Dibuat sendiri dengan Python (numpy) untuk proyek ini, jadi bebas dipakai.
Skrip pembuatnya berupa gelombang sinus pendek: klik halus, dua nada naik
untuk jawaban benar, dua nada turun untuk jawaban salah, dan geser nada
naik untuk petunjuk.

  klik.wav   bunyi tombol (style button, lewat 07_audio.rpy)
  benar.wav  jawaban benar
  salah.wav  jawaban salah
  hint.wav   saat petunjuk dipakai

Catatan
-------
- Volume semua efek suara diatur satu angka di 07_audio.rpy:
  define PK_VOLUME_SFX = 0.5   (1.0 = sekeras berkas aslinya)
  Musik latar tidak ikut terpengaruh; volume musik tetap di menu Pengaturan.
- Berkas di sini dijalankan oleh fungsi putar_musik() dan putar_suara() di
  07_audio.rpy. Keduanya cek dulu berkasnya ada; kalau hilang, game tetap
  jalan tanpa suara.
- Kalau kamu ganti lagu, pakai nama berkas yang sama supaya tidak perlu
  mengubah kode. Format yang aman: .ogg, .mp3, atau .wav.
