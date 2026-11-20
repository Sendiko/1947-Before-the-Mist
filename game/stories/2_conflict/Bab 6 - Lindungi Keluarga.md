# Lindungi Keluarga: Narasi dan Dialog Gameplay

Babak 2, setelah Bab 5 (pilihan 3: Lereng Gunung Slamet, Baseh)

## Catatan Desain

Setiap hari Lindungi Keluarga terdiri dari dua misi: **Hujan Meriam** (grid ala Battleship) dan **Bagi Jatah** (fase tenang di antara tembakan). Kesulitan naik setiap hari.

| Hari | Tingkat | Hujan Meriam                                            | Bagi Jatah           |
| ---- | ------- | ------------------------------------------------------- | -------------------- |
| 1    | Mudah   | 4 unit biru, 4 salvo, 1 sampai 2 marker merah per salvo | 3 kebutuhan, 3 jatah |
| 2    | Sedang  | 6 unit biru, 5 salvo, 2 sampai 3 marker per salvo       | 4 kebutuhan, 3 jatah |
| 3    | Sulit   | 8 unit biru, 6 salvo, 3 sampai 4 marker per salvo       | 5 kebutuhan, 4 jatah |

### Aturan Hujan Meriam

- **Grid 4x4** (kolom A sampai D, baris 1 sampai 4) mewakili petak-petak kebun di lereng Baseh. Marker **biru** adalah Ibu, Adik, dan para warga. Satu petak hanya boleh diisi satu unit.
- Setiap salvo, marker **merah** muncul acak di beberapa petak dengan **timer 3 detik** (lingkaran menyusut, disertai siulan peluru). Pemain **menyeret (drag)** marker biru yang berada di petak merah ke petak aman (tidak merah, tidak terisi unit lain).
- Saat timer habis, setiap petak merah meledak. Petak merah yang kosong atau yang sudah dikosongkan: **meleset**. Unit biru yang masih berada di petak merah: **terkena**.
- Generator salvo selalu menyisakan cukup petak aman, jadi setiap salvo **selalu bisa diselamatkan** sepenuhnya. Kesulitan datang dari banyaknya unit yang harus dipindah dalam 3 detik.
- Jeda antar salvo 1,5 detik (marker merah hilang, unit boleh dirapikan).
- **Terkena:** terkena pertama dan kedua memunculkan dialog peringatan. **Terkena ketiga berarti gagal** (sisa salvo dibatalkan dan warga dievakuasi paksa ke parit). Setiap unit yang terkena dihitung satu kali.
- **Berhasil sempurna:** semua salvo selesai tanpa satu pun unit terkena. Memberi **Ikatan Keluarga++**.
- **Cangkang keong:** di salah satu jeda salvo, satu cangkang keong bercahaya muncul di petak kosong selama 3 detik. Ketuk untuk mengambilnya (1 per hari). Cangkang yang bertemu petak merah akan hilang.
- **Bonus intel Telik Sandi:** jika pemain memiliki intel “Tembakan artileri ke lereng selatan setiap fajar pukul 05.00”, marker merah pertama di tiap salvo muncul dengan timer **4 detik**.
- Gagal bukan game over. Sumarno selalu selamat, tetapi ada warga yang terluka parah dan Ikatan Keluarga tidak naik.
- Teks dalam _(kurung miring)_ adalah isyarat UI atau percabangan, bukan dialog.

### Aturan Bagi Jatah

- Fase tenang setelah salvo terakhir. Layar menampilkan beberapa **kebutuhan** (Makanan, Air, Obat, dan seterusnya) dan sejumlah **token jatah**. Pemain menyeret token ke kebutuhan yang ingin dipenuhi.
- Hari 1 jatah cukup untuk semua. Hari 2 dan 3 jatah **kurang satu**, sehingga pemain harus memilih siapa yang didahulukan.
- **Rampasan dari Penyergapan** menambah token (+1 per jenis rampasan yang cocok: ransum, obat, selimut, garam).
- **Sempurna:** semua kebutuhan terpenuhi. Kebutuhan yang tidak terpenuhi dicatat di Laporan.

Contoh jumlah petak aman (Hujan Meriam), jika semua unit di petak merah:

| Hari | Unit | Marker merah | Petak kosong tersedia |
| ---- | ---- | ------------ | --------------------- |
| 1    | 4    | 1 sampai 2   | 12                    |
| 2    | 6    | 2 sampai 3   | 10                    |
| 3    | 8    | 3 sampai 4   | 8                     |

---

## HARI 1: “Petak Kebun” (Mudah)
### **Scene 1.0** EXT. Posko Evakuasi, Desa Baseh - Menjelang Subuh
#### Pemain: Sumarno, Paman, Ibu, Adik, Pak Lurah, Warga Pengungsi

Kabut turun pekat. Sumarno dan Paman muncul dari jalur tikus, napas mengepul. Ibu yang sedang menyalakan tungku di dapur umum menoleh, lalu menjatuhkan sendok kayunya.

**Ibu** Marno? Kamu kembali?

**Sumarno** Marno ikut Paman, Bu. Marno tidak mau jauh dari Ibu dan Adik.

_(Jika Sumarno ikut Pasukan Laskar di Bab 2)_

**Ibu** (Menyentuh baju Sumarno) Bau bensinnya sudah hilang. Tapi Ibu tahu kamu masih membawa api itu di dadamu.

_(Jika Sumarno ikut Paman di Bab 2)_

**Ibu** (Memeluknya erat) Ibu lega kamu kembali. Tapi Ibu juga tahu kamu tidak datang untuk duduk diam.

Adik berlari dan memeluk kaki Sumarno. Tangannya menunjuk saku dada kakaknya.

**Adik** Kak, kereta apinya masih ikut jaga Kakak?

**Sumarno** (Menepuk saku) Masih, Dik. Dia rajin sekali.

Paman menarik Pak Lurah ke tengah balai bambu. Dengan ranting, ia menggambar kotak-kotak di tanah: empat kali empat.

**Paman** Semalam Paman hitung. Meriam mereka menembak tiap pukul lima. Dari kilatan di kota sampai pelurunya jatuh di sini, siulannya tiga hitungan. Tiga hitungan, itu waktu kita.

**Pak Lurah** Lereng ini kita bagi jadi enam belas petak. Satu petak, satu keluarga. Yang berdiri di petak yang ditunjuk, pindah.

**Paman** No, kamu paling gesit. Kamu pengawas petak. Teriakkan yang terancam, bantu mereka berpindah.

**Sumarno** (Menatap kotak-kotak itu) Seperti main petak umpet dengan Adik. Hanya saja yang jaga membawa meriam.

_(Tutorial: seret marker biru dari petak merah ke petak aman sebelum lingkaran habis.)_

### **Scene 1A-1** EXT. Lereng Baseh - Subuh, Pukul 05.00
#### Misi Hujan Meriam | Pemain: Sumarno, Paman, Ibu, Adik, Warga

Siulan panjang membelah fajar. Dari kejauhan, kilatan oranye berkedip di arah kota.

_(Total 4 salvo. Marker merah muncul 1 sampai 2 per salvo. Timer 3 detik. Seret unit biru ke petak aman.)_

**Paman** (Berteriak) Petak merah! Pindah! Pindah!

**Sumarno** (Batin) Tiga hitungan. Satu, dua...

#### Peringatan 1 (unit terkena pertama)
Dentuman mengguncang lereng. Seorang warga terpental dan memegangi lengannya yang berdarah. Debu dan serpihan bambu berhamburan.

**Warga Pengungsi** (Meringis) Pecahan! Saya tidak apa-apa, cepat pindah ke yang lain!

**Paman** (Tajam) Jangan melamun, No! Lihat cincinnya, jangan dengar tangisnya!

_(Peringatan 1/2)_

_(Varian jika yang terkena Ibu atau Adik)_ Debu menutup mata Sumarno. Saat ia berkedip, Ibu terjatuh dengan lutut berdarah, Adik menjerit di sampingnya. **Sumarno** (Panik) Ibu! Adik! **Ibu** (Menahan sakit) Ibu tidak apa-apa, No. Selamatkan yang lain dulu!

#### Peringatan 2 (unit terkena kedua)
Peluru kedua jatuh lebih dekat. Seorang nenek terhuyung dan dipapah dua warga ke kolong balai.

**Paman** (Berbisik, rahangnya mengeras) Dua kali, No. Kalau tiga, kita tidak sempat mengevakuasi semuanya.

_(Peringatan 2/2. Satu terkena lagi berarti gagal.)_

#### Gagal (terkena ketiga)
Sebuah ledakan menghantam petak di dekat dapur umum. Warga berhamburan tanpa arah.

**Pak Lurah** (Berteriak) Semua masuk parit! Sekarang!

Sumarno menarik Adik dan Ibu ke parit, menutup tubuh mereka dengan badannya sampai dentuman terakhir mereda.

**Sumarno** (Batin, terengah) Aku terlalu lambat... Aku tidak bisa menyelamatkan semua.

_(Hujan Meriam gagal. Lanjut ke Scene 1B-1 dengan varian “kekurangan”: kebutuhan Obat +1)_

#### Berhasil
Salvo terakhir jatuh di lereng kosong. Yang tersisa hanya debu, bau mesiu, dan hening.

**Paman** (Menghela napas) Empat salvo, semuanya selamat. Kamu belajar cepat, No.

_(Jika tanpa terkena sama sekali)_

**Pak Lurah** Tidak ada yang tergores? Marno, kamu ini anak lurah atau anak malaikat?

_(Ikatan Keluarga++ jika sempurna)_

### **Scene 1B-1** EXT. Dapur Umum, Balai Bambu - Pagi
#### Misi Bagi Jatah | Pemain: Sumarno, Ibu, Adik, Warga

Pagi merayap di antara kabut. Bubur encer mengepul di panci besar. Ibu dan para ibu lain menunggu keputusan Sumarno. Di meja, ada tiga token jatah.

_(Hari 1: 3 kebutuhan: Makanan Anak-anak, Air Bersih, Obat Luka. 3 token jatah. Seret token ke kebutuhan.)_

**Ibu** Biar Ibu yang bagi, No. Kamu cukup bilang mana yang paling mendesak.

**Sumarno** (Menimbang) Adik dan anak-anak dulu. Setelah itu air, lalu obat untuk yang terluka tadi.

_(Jika semua kebutuhan terpenuhi)_

**Ibu** (Tersenyum) Hari ini cukup untuk semuanya. Syukurlah.

_(Jika ada yang tidak terpenuhi)_

**Ibu** (Pelan) Besok kita cari lebih banyak, No. Sisanya kita bagi rata.

### **Scene 1.9** EXT. Balai Bambu, Posko Baseh - Senja
#### Laporan | Pemain: Sumarno, Paman, Ibu, Adik

_(Sempurna: tanpa terkena, jatah penuh)_

**Paman** Tidak ada yang hilang hari ini. Tapi besok mereka akan menembak lebih dekat.

**Sumarno** (Menatap Adik yang menyusun batu kecil) Marno siap, Paman.

_(Cukup: 1 terkena)_

**Paman** Satu luka kecil, itu harga yang bisa kita bayar. Besok lebih baik lagi.

_(Minim: 2 terkena)_

**Paman** Dua orang terluka, No. Tapi mereka masih hidup. Itu yang paling penting.

_(Gagal)_

**Ibu** (Mengusap kepala Sumarno) Kamu sudah berusaha, No. Besok kita coba lagi.

**Sumarno** (Menunduk) Maaf, Bu.

---

## HARI 2: “Siulan di Atas Kabut” (Sedang)
### **Scene 2.0** EXT. Posko Evakuasi, Desa Baseh - Malam
#### Pemain: Sumarno, Paman, Pak Lurah, Mantri Karto

Tenda-tenda lebih padat. Beberapa pengungsi baru datang dari Karangnangka dengan wajah penuh debu.

**Pak Lurah** Kemarin cuma enam petak yang dipakai. Besok bisa dua belas. Peluru mereka makin berani turun ke lembah.

**Mantri Karto** (Mengusap peluh) Saya butuh obat lebih banyak, Pak. Luka kemarin sudah mulai bernanah.

_(Jika pemain sudah menyelesaikan Penyergapan Hari 2 dan mendapat “Obat dan perban”)_

**Sumarno** Mantri, ini dari kawan-kawan di rel. Perban dan kina untuk lukanya.

**Mantri Karto** (Terkejut) Kamu membawa ini dari kota? Tuhan masih menyisakan jalan.

**Paman** Besok pukul lima, No. Siulannya tetap tiga hitungan, tapi kali ini lebih banyak yang harus kamu pindahkan.

### **Scene 2A-1** EXT. Lereng Baseh - Subuh, Pukul 05.00
#### Misi Hujan Meriam | Pemain: Sumarno, Paman, Ibu, Adik, Warga

Kabut tipis tak lagi cukup menyembunyikan tenda. Siulan pertama membelah langit.

_(Total 5 salvo. Marker merah muncul 2 sampai 3 per salvo. 6 unit biru. Timer 3 detik.)_

**Sumarno** (Batin) Enam orang di enam petak. Aku tidak boleh salah menghitung.

#### Peringatan 1 (unit terkena pertama)
Sebuah peluru jatuh tepat di tepi kebun. Seorang bapak jatuh tersungkur dan dipapah ke kolong balai.

**Paman** (Berteriak) Fokus, No! Satu lagi dan mereka tidak akan berhenti!

_(Peringatan 1/2)_

#### Peringatan 2 (unit terkena kedua)
Serpihan bambu menggores wajah seorang ibu muda. Bayinya menjerit.

**Ibu** (Memeluk bayi itu, lirih) Marno, jangan lihat kami. Lihat petaknya.

_(Peringatan 2/2. Satu terkena lagi berarti gagal.)_

#### Gagal (terkena ketiga)
Sebuah dentuman besar mengguncang balai bambu. Atapnya miring dan debu menutup pandangan.

**Pak Lurah** Masuk parit! Cepat!

Sumarno menyeret anak-anak ke dalam parit, menutup telinga mereka dengan telapak tangannya.

**Sumarno** (Batin) Kenapa tiga hitungan begitu pendek?

_(Hujan Meriam gagal. Lanjut ke Scene 2B-1 dengan varian “kekurangan”: kebutuhan Obat +1)_

#### Berhasil
Setelah salvo terakhir, lereng Baseh kembali senyap. Para warga keluar dari parit dan saling memeriksa.

**Paman** (Mengangguk pelan) Bagus, No. Mayer mulai kehilangan kesabaran.

_(Jika tanpa terkena sama sekali)_

**Pak Lurah** Lima salvo tanpa luka. Kalau semua pengawas seperti kamu, kami bisa tidur nyenyak.

_(Ikatan Keluarga++ jika sempurna)_

### **Scene 2B-1** EXT. Dapur Umum, Balai Bambu - Pagi
#### Misi Bagi Jatah | Pemain: Sumarno, Ibu, Mantri Karto, Warga

Persediaan menipis. Panci bubur sudah terlihat dasarnya. Ada empat kebutuhan, tapi hanya tiga token jatah.

_(Hari 2: 4 kebutuhan: Makanan Anak-anak, Air Bersih, Obat Luka, Selimut. 3 token jatah, +1 per rampasan cocok dari Penyergapan.)_

**Mantri Karto** (Pelan) Kita tidak bisa memenuhi semuanya, Marno. Siapa yang kamu pilih?

**Sumarno** (Menarik napas) Mereka yang paling lemah dulu. Sisanya kita cari lagi.

_(Jika ada rampasan cocok)_

**Ibu** (Menatap Sumarno) Ada yang lebih dari yang Ibu kira. Dari mana?

**Sumarno** Dari teman-teman, Bu.

### **Scene 2.9** EXT. Balai Bambu, Posko Baseh - Senja
#### Laporan | Pemain: Sumarno, Paman, Ibu, Pak Lurah

_(Sempurna)_

**Pak Lurah** Dua hari berturut-turut tanpa korban. Orang-orang mulai percaya pada petak-petakmu, No.

**Paman** Besok yang terberat. Kolonel Mayer tidak suka kalah.

_(Cukup: 1 terkena)_

**Paman** Satu orang terluka. Tapi masih ada kesempatan besok.

_(Minim: 2 terkena)_

**Pak Lurah** Dua orang terluka, tapi kita masih berdiri. Itu cukup.

_(Gagal)_

**Ibu** Besok kita bangun lagi, No. Kamu tidak sendirian.

---

## HARI 3: “Salvo Penutup” (Sulit)
### **Scene 3.0** EXT. Posko Evakuasi, Desa Baseh - Malam
#### Pemain: Sumarno, Paman, Ibu, Adik, Pak Lurah

Pak Lurah mengumpulkan semua warga di balai. Wajah-wajah lelah, tapi tak ada yang beranjak.

**Pak Lurah** Besok mereka menembak dengan semua yang mereka punya. Delapan petak harus berpindah dalam satu napas.

**Sumarno** Marno yang mengomando, Pak. Marno janji tidak akan ada yang tertinggal.

**Adik** (Menarik baju Sumarno) Kak, kalau besok Kakak tidak pulang, kereta apinya ikut tidak pulang?

**Sumarno** (Berjongkok, tersenyum) Kereta apinya akan pulang bersama Kakak. Dengan gerbong-gerbong baru.

_(Jika Sumarno ikut Pasukan Laskar di Bab 2)_

**Paman** Kamu menyalakan api di kota. Besok, kamu padamkan ketakutan di sini.

_(Jika Sumarno ikut Paman di Bab 2)_

**Paman** Kamu menahan diri demi mereka. Besok, buktikan itu bukan sia-sia.

### **Scene 3A-1** EXT. Lereng Baseh - Subuh, Pukul 05.00
#### Misi Hujan Meriam | Pemain: Sumarno, Paman, Ibu, Adik, Warga

Siulan paling nyaring terdengar dari kota. Kali ini bukan satu, melainkan beruntun.

_(Total 6 salvo. Marker merah muncul 3 sampai 4 per salvo. 8 unit biru. Timer 3 detik.)_

**Paman** (Berteriak) Semua petak! Jangan berhenti bergerak!

**Sumarno** (Batin) Delapan. Empat petak merah. Satu, dua, tiga...

#### Peringatan 1 (unit terkena pertama)
Tanah bergetar hebat. Seorang bapak terjatuh, dan warga lain segera menariknya ke parit.

**Pak Lurah** (Berteriak) Marno! Jangan berhenti!

_(Peringatan 1/2)_

#### Peringatan 2 (unit terkena kedua)
Dua peluru jatuh nyaris bersamaan. Debu menutup langit, dan terdengar jeritan di antara kabut.

**Paman** (Parau) Satu lagi, No, dan semuanya hancur!

_(Peringatan 2/2. Satu terkena lagi berarti gagal.)_

#### Gagal (terkena ketiga)
Sebuah ledakan menyapu seluruh petak bawah. Warga berhamburan masuk parit tanpa aba-aba.

**Sumarno** (Batin, tersengal) Aku tidak sanggup... mereka terlalu banyak.

Ibu menarik Sumarno ke dalam parit, memeluknya erat.

**Ibu** Cukup, No. Kamu sudah berjuang. Biarkan sisanya kita hadapi bersama.

_(Hujan Meriam gagal. Lanjut ke Scene 3B-1 dengan varian “kekurangan”: kebutuhan Obat +1)_

#### Berhasil
Salvo terakhir jatuh. Hening panjang menyelimuti lereng. Perlahan, para warga keluar dari parit.

**Pak Lurah** (Terisak) Semuanya selamat. Semuanya.

**Sumarno** (Batin, menatap telapak tangannya) Aku tidak menyalakan api kali ini. Aku memadamkannya.

_(Jika tanpa terkena sama sekali)_

**Paman** (Menepuk bahu Sumarno) Kamu bukan lagi keponakan Paman, No. Kamu penjaga mereka semua.

_(Ikatan Keluarga++ jika sempurna)_

### **Scene 3B-1** EXT. Dapur Umum, Balai Bambu - Pagi
#### Misi Bagi Jatah | Pemain: Sumarno, Ibu, Adik, Mantri Karto, Warga

Tak ada yang bicara. Dapur umum nyaris kosong. Ada lima kebutuhan dan hanya empat token jatah.

_(Hari 3: 5 kebutuhan: Makanan Anak-anak, Air Bersih, Obat Luka, Selimut, Makanan Lansia. 4 token jatah, +1 per rampasan cocok.)_

**Ibu** (Pelan) Kita punya sedikit, tapi kita punya satu sama lain.

**Sumarno** (Mengambil token terakhir) Biar yang paling lemah makan dulu.

_(Jika semua kebutuhan terpenuhi)_

**Mantri Karto** (Tersenyum lelah) Tiga hari berturut-turut, tak ada yang kelaparan. Ini keajaiban kecil.

_(Jika ada yang tidak terpenuhi)_

**Mantri Karto** Kita akan bertahan, Nak. Dengan cara kita sendiri.

### **Scene 3.9** EXT. Balai Bambu, Posko Baseh - Senja
#### Laporan | Pemain: Sumarno, Paman, Ibu, Adik

_(Sempurna)_

**Ibu** (Mengusap pipi Sumarno) Tiga hari, tidak ada yang hilang. Ibu bangga, No.

**Adik** (Menyodorkan batu kecil) Kak, ini gerbong baru. Tapi masih belum sepanjang yang dulu.

**Sumarno** (Tersenyum, menahan tangis) Nanti Kakak buatkan yang lebih panjang, Dik.

_(Cukup: 1 terkena)_

**Paman** Satu luka kecil dari tiga hari yang panjang. Kamu sudah melakukan yang terbaik.

_(Minim: 2 terkena)_

**Paman** Dua orang terluka, No. Tapi mereka masih hidup. Itu yang terpenting.

_(Gagal)_

**Ibu** (Lembut) Mereka tidak menyalahkanmu, No. Kami semua masih di sini.

**Sumarno** (Menunduk) Marno akan lebih baik, Bu.