# Telik Sandi: Narasi dan Dialog Gameplay
Babak 2, setelah Bab 5 (pilihan 1: Jalan-jalan Kota)

## Catatan Desain
Setiap hari Telik Sandi terdiri dari dua misi: **Antar Logistik** dan **Menyusup Menguping**. Kesulitan naik setiap hari.

| Hari | Tingkat | Antar Logistik                                                   | Menyusup                                  |
| ---- | ------- | ---------------------------------------------------------------- | ----------------------------------------- |
| 1    | Mudah   | Bakul jamu ke rumah Pak Tahu, 3 titik, penjaga menoleh pelan     | Pos jaga di Pasar                         |
| 2    | Sedang  | Perban dan obat ke surau tepi sungai, 5 titik, penjaga bersenter | Pos komunikasi di bekas rumah dinas       |
| 3    | Sulit   | Beras ke pos hutan, 7 titik, penjaga waspada dan cepat menoleh   | Gedung Pemerintahan, markas Kolonel Mayer |

Aturan yang dipakai:
- **Antar Logistik:** tahan SPASI untuk maju, lepas saat penjaga menoleh. Ketahuan pertama dan kedua memunculkan dialog peringatan, ketahuan ketiga berarti gagal. Berhasil memberi Intel++.
- **Menyusup:** ada 5 dialog prajurit Belanda dan 4 menu Tetap/Mundur dengan risiko terlihat 15%, 40%, 65%, 90%. Dialog pertama gratis, setiap dialog yang berhasil didengar memberi Intel++. Mendengar kelima dialog dihitung sempurna.
- Gagal bukan game over. Sumarno selalu lolos, tetapi logistik hilang atau intel tidak sampai ke markas.
- Percakapan Belanda ditulis dalam Bahasa Indonesia sebagai terjemahan batin Sumarno (ia belajar bahasa Belanda di sekolah). Bisa ditambah frasa Belanda pendek sebagai rasa.
- Teks dalam _(kurung miring)_ adalah isyarat UI atau percabangan, bukan dialog.

---
## HARI 1: “Bakul Jamu” (Mudah)
### **Scene 1.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Ibu Jamu

Ibu Jamu meletakkan sebuah bakul anyaman di pangkuan Sumarno. Aroma kunyit dan jahe menyengat. Di bawah deretan botol, terselip belasan nasi bungkus.

**Ibu Jamu** Botol di atas, nasi di bawah. Kalau ada yang bertanya, kamu anak saya yang bantu jualan.

**Sumarno** (Tersenyum kecil) Sudah lama tidak ada yang memanggil saya begitu, Bu.

**Komandan Laskar** Dua tugas malam ini, Marno. Antar bakul itu ke rumah Pak Tahu di ujung gang, orang kita di sana belum makan dua hari. Lalu menyusup ke pos jaga di pasar. Di sana kamu hanya mendengar. Tidak lebih.

**Sumarno** Siap, Komandan.

### **Scene 1A-1** EXT. Gang Belakang Pasar - Malam
#### Misi Antar Logistik | Pemain: Sumarno, Soldat Hendrik

Kabut menggantung rendah. Di ujung jalan, Soldat Hendrik bersandar pada tiang lampu yang padam, senapannya tersampir malas di bahu. Ia sering menguap, dan sesekali menoleh tanpa pola.

_(Hendrik membelakangi: tahan SPASI untuk melangkah. Hendrik menoleh: lepas SPASI.)_

**Sumarno** (Batin) Jalan saat ia membelakangi, diam saat ia menoleh. Seperti petak umpet dengan Adik, hanya saja yang jaga kali ini membawa senapan.

#### Peringatan 1 (ketahuan pertama)

Hendrik berbalik tiba-tiba. Sumarno mematung dengan satu kaki masih terangkat, bakul bergoyang di lengannya.

**Hendrik** Hei, kamu! Siapa di sana?

**Sumarno** Jamu, Tuan. Jamu pegal linu, kunyit asam.

Hendrik menyipitkan mata, lalu menguap lebar.

**Hendrik** Jam segini jual jamu? Pergi sana. Jangan lewat sini lagi.

_(Peringatan 1/2)_

#### Peringatan 2 (ketahuan kedua)

Hendrik melangkah mendekat dan mengangkat kain penutup bakul dengan ujung laras. Botol-botol berdenting. Nasi bungkus di dasar bakul tersembunyi tepat di bawah jari-jarinya.

**Hendrik** Baunya aneh. Apa ini?

**Sumarno** (Menahan gemetar) Kunyit asam, Tuan. Coba seteguk, bagus untuk perut.

Hendrik ragu, lalu mencicipi. Wajahnya langsung mengerut.

**Hendrik** Mengerikan! Bawa pergi! Sekali lagi kamu muncul di depan mataku, bakulmu kuperiksa sampai dasar.

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)

Hendrik tidak bertanya lagi. Ia menyambar bakul dan menyibak seluruh kain penutupnya. Nasi bungkus berhamburan ke tanah basah.

**Hendrik** Ini bukan jamu! Berhenti!

Peluit melengking membelah kabut. Sumarno melepas bakul dan menerobos lorong sempit di antara lapak, dadanya berdentum. Satu tembakan peringatan meledak ke udara, tapi langkah sepatu bot di belakangnya berhenti di mulut gang.

**Sumarno** (Batin, terengah) Nasinya... orang-orang di rumah Pak Tahu masih menunggu.

_(Logistik gagal terkirim)_

#### Berhasil

Tiga ketukan, jeda, satu ketukan. Pintu rumah Pak Tahu terbuka sedikit, lalu tertutup cepat di belakang Sumarno. Di ruang bawah tanah, enam orang berbaju lusuh menatap bakul itu seperti menatap harta karun.

**Pak Tahu** Masuk, masuk! Ibu Jamu memang tidak pernah salah memilih orang.

**Pejuang** (Mengunyah pelan) Dua hari kami cuma minum air sumur. Terima kasih, Nak.

Pak Tahu menepuk bahu Sumarno.

**Pak Tahu** Hati-hati pulangnya. Jangan lewat jalan yang sama.

_(Intel++)_

_(Jika tanpa Peringatan sama sekali)_

**Pak Tahu** Tidak ketahuan sekali pun? Lama-lama kamu pantas dijuluki Si Kabut.

### **Scene 1B-1** EXT. Pos Jaga Pasar - Tengah Malam
#### Misi Menyusup | Pemain: Sumarno, Sersan Willem, Kopral Pieter

Sumarno merayap ke ruang sempit di balik tumpukan keranjang bambu, tiga langkah dari meja jaga. Sersan Willem dan Kopral Pieter duduk mengitari lampu petromaks, bicara dalam bahasa Belanda. Sumarno hampir tak percaya: pelajaran yang dulu ia anggap sia-sia kini menjadi telinganya.

**Sersan Willem** Kabut sialan. Aku tidak bisa melihat ujung jalan.

**Kopral Pieter** Tenang, Sersan. Pribumi tidak berani keluar kalau kabut begini.

**Sersan Willem** Justru itu. Pergantian jaga tepat tengah malam, jangan ada yang tertidur sebelumnya.

_(Intel++: Pergantian jaga pasar tepat tengah malam)_

_(Menu, risiko terlihat 15%: 1. Tetap, dengarkan lagi / 2. Mundur pelan-pelan)_

Sumarno menahan napas. Tidak ada yang menoleh.

**Kopral Pieter** Kenapa kita hanya mengawasi jalan raya? Gang belakang pasar tidak pernah diperiksa.

**Sersan Willem** Terlalu sempit untuk truk. Biarkan tikus-tikus itu berlarian di sana.

_(Intel++: Gang belakang pasar tidak diawasi)_

_(Menu, risiko terlihat 40%)_

Sebatang bambu berderak di bawah lutut Sumarno. Willem melirik sekilas, lalu kembali ke cangkir kopinya.

**Kopral Pieter** Truk dari pelabuhan utara datang lagi lusa?

**Sersan Willem** Dua truk dan satu jip pengawal, lewat jalan lingkar timur sebelum subuh. Jangan tanya lagi, aku bukan juru bicara.

_(Intel++: Konvoi logistik lusa, jalan lingkar timur sebelum subuh)_

_(Menu, risiko terlihat 65%)_

Keringat dingin menetes ke dagu Sumarno. Ia tidak berani mengusapnya.

**Kopral Pieter** (Merendahkan suara) Benar besok pagi kelurahan timur digeledah?

**Sersan Willem** Rumah demi rumah, perintah Kolonel. Kalau ada pemuda bersembunyi, bawa ke sini.

_(Intel++: Penggeledahan kelurahan timur besok pagi)_

_(Menu, risiko terlihat 90%)_

Lampu petromaks berdesis. Sumarno nyaris bisa mendengar jantungnya sendiri.

**Sersan Willem** (Mengeluarkan selembar kertas) Daftar dari Kolonel. Guru, pegawai kantor pos, kepala stasiun. Semua yang pernah bekerja untuk Republik.

**Kopral Pieter** Guru sekolah rakyat dekat alun-alun, yang rumahnya berpagar kayu, sudah kabur ke gunung, Sersan.

**Sersan Willem** Tidak masalah. Orang yang lari lebih mudah dicari daripada yang bersembunyi.

Sumarno membeku. Rumah berpagar kayu. Pak Guru.

_(Intel++: Daftar buruan sipil Republik, termasuk Pak Guru)_

#### Ketahuan (dari menu mana pun)

Siku Sumarno menyenggol tumpukan keranjang. Satu keranjang jatuh dan berguling nyaring di atas aspal.

**Sersan Willem** Siapa di sana?!

Senter menyapu kabut. Sumarno melompat keluar dan berlari.

_(Jika sudah mendapat intel “Gang belakang pasar tidak diawasi”)_ Ia membelok ke gang yang tadi mereka bicarakan. Benar saja, tak seorang pun menunggu. Langkah sepatu bot menghilang di belakangnya.

_(Jika belum)_ Ia berlari buta di antara lapak dan meringkuk di kolong sampai suara sepatu bot menjauh.

Sumarno tiba di markas dengan tangan kosong dan paru-paru terbakar.

_(Menyusup gagal)_

#### Mundur

**Sumarno** (Batin) Cukup. Pulang membawa sedikit lebih baik daripada tidak pulang.

Ia merayap mundur lewat sela keranjang sampai bayangan Belanda lenyap di balik kabut.

### **Scene 1.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar

_(Sempurna, 5 intel)_

**Komandan Laskar** Lima catatan, tak satu pun meleset. Ada apa dengan wajahmu?

**Sumarno** Ada nama Pak Guru di daftar mereka, Komandan.

**Komandan Laskar** Kosongkan setiap rumah yang tercatat sebelum fajar. Malam ini kamu menjadi mata kami, Marno.

_(Cukup, 3 sampai 4 intel)_

**Komandan Laskar** Cukup. Berhenti di saat yang tepat juga sebuah keahlian. Jalur konvoi dan jadwal penggeledahan ini sangat berguna.

_(Minim, 1 sampai 2 intel)_

**Komandan Laskar** Sedikit, tapi benar. Yang serakah biasanya tidak pulang untuk melapor.

_(Gagal)_

**Komandan Laskar** Kamu hidup. Itu kabar paling penting malam ini. Besok kita coba lagi.

**Sumarno** (Menunduk) Maaf, Komandan.

---

## HARI 2: “Senter di Tengah Kabut” (Sedang)
### **Scene 2.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Ibu Jamu

Ibu Jamu mengikat bungkusan berisi perban dan kina ke dalam gendongan kain, lalu menimbunnya dengan setandan pisang.

**Komandan Laskar** Mantri Karto menunggu di surau tua tepi sungai. Dua orang kita terkena pecahan meriam di lereng. Tanpa perban, lukanya membusuk. Rutenya lebih panjang dari kemarin, dan Belanda sudah mulai memakai senter.

**Sumarno** Setelah itu, Komandan?

**Komandan Laskar** Pos komunikasi di bekas rumah dinas Asisten Residen. Dengarkan siapa bicara dengan siapa.

### **Scene 2A-1** EXT. Jalan Tepi Sungai - Malam
#### Misi Antar Logistik | Pemain: Sumarno, Kopral Gerrit

Kabut lebih tipis malam ini. Kopral Gerrit berjalan mondar-mandir sambil menyapukan senter ke kiri dan kanan. Ia menoleh lebih sering, dan lebih cepat.

_(Gerrit membelakangi: tahan SPASI. Gerrit menoleh: lepas SPASI. Lima titik menuju surau.)_

**Sumarno** (Batin) Lima titik sampai surau. Cahaya itu tidak mengenal ampun.

#### Peringatan 1 (ketahuan pertama)

Cahaya senter jatuh tepat di wajah Sumarno. Ia mematung, gendongan pisang terasa berat bagai batu.

**Gerrit** Jam malam sudah lewat. Mau ke mana?

**Sumarno** Cari pisang matang untuk Ibu yang sedang sakit, Tuan.

**Gerrit** Pisang, jam segini? Pulang sebelum kesabaranku habis.

_(Peringatan 1/2)_

#### Peringatan 2 (ketahuan kedua)

Gerrit menghampiri, merogoh gendongan, mengambil sebuah pisang dan mengupasnya. Jarinya hanya terpaut selapis kain dari bungkusan perban.

**Gerrit** (Mengunyah) Pajak jalanan. Ini terakhir kali aku bermurah hati, Nak.

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)

Gerrit mengerutkan dahi. Gendongan itu terlalu berat untuk sekadar pisang. Ia menyobek kainnya, dan perban serta kina terguling ke lumpur.

**Gerrit** Perban! Pemberontak!

Peluit. Senter menyorot liar. Sumarno terjun ke parit dan merangkak dalam air dingin sampai suara sepatu hilang di kejauhan.

**Sumarno** (Batin, menggigil) Mantri Karto pasti menunggu sampai fajar. Dan orang-orang yang terluka itu...

_(Logistik gagal terkirim)_

#### Berhasil

Surau tua itu hanya diterangi lampu minyak yang redup. Dua laskar terbaring di tikar, satu dengan kaki terbalut kain sarung yang sudah merah.

**Mantri Karto** (Membuka bungkusan, mengembuskan napas) Kina dan perban. Tuhan masih menyisakan jalan.

**Laskar Terluka** (Meringis, tersenyum) Anak muda, kamu lewat di bawah senter itu seperti bayangan.

**Mantri Karto** Kamu membawa lebih dari perban, Nak. Kamu membawa alasan supaya mereka tetap hidup.

_(Intel++)_

_(Jika tanpa Peringatan sama sekali)_

**Laskar Terluka** Tak sekali pun senter itu mengenaimu? Setelah lukaku sembuh, ajari aku caranya.

### **Scene 2B-1** EXT. Rumah Dinas Bekas Asisten Residen - Tengah Malam
#### Misi Menyusup | Pemain: Sumarno, Letnan de Vries, Soldat Jan

Rumah besar bergaya kolonial itu kini dililit kabel yang merambat dari tiang di jalan lingkar. Sumarno bersembunyi di kolong teras panggung, tepat di bawah kursi tempat Letnan de Vries dan operator Jan duduk. Debu turun dari celah papan setiap kali kursi bergeser.

**Soldat Jan** (Memutar engkol telepon) Hanya satu kabel ke Banyumas, Letnan, lewat tiang di jalan lingkar. Kalau putus, kita tuli.

**Letnan de Vries** Maka jangan sampai putus.

_(Intel++: Satu-satunya kabel telepon militer lewat tiang jalan lingkar)_

_(Menu, risiko terlihat 15%: 1. Tetap, dengarkan lagi / 2. Mundur pelan-pelan)_

Sumarno menahan napas. Kursi di atasnya berderit, lalu diam.

**Letnan de Vries** Setelah isya ada dua operator berjaga. Lewat tengah malam tinggal kau seorang, Jan.

**Soldat Jan** Dan siapa yang menjagaku?

**Letnan de Vries** Senapanmu.

_(Intel++: Lewat tengah malam hanya satu operator berjaga)_

_(Menu, risiko terlihat 40%)_

Seekor kecoak merayap di lengan Sumarno. Ia membiarkannya.

**Soldat Jan** Laporan radio ke Semarang tiap pukul dua. Kolonel Mayer sendiri yang membacakan naskahnya.

_(Intel++: Laporan radio harian pukul 02.00)_

_(Menu, risiko terlihat 65%)_

Keringat dingin menuruni punggung Sumarno. Papan di atasnya berderak.

**Letnan de Vries** Kolonel tidak sabar. Ia ingin meriam dipindah lebih dekat ke alun-alun. Dari sana jangkauan ke lereng lebih mudah.

**Soldat Jan** Dan para pengungsi?

**Letnan de Vries** Itu urusan mereka.

_(Intel++: Meriam akan dipindah dekat alun-alun)_

_(Menu, risiko terlihat 90%)_

Lampu di atas bergoyang. Bayangan kaki kursi menari di wajah Sumarno.

**Letnan de Vries** (Membuka map) Perintah baru. Mulai fajar besok, tembakkan salvo ke lereng selatan setiap hari pukul lima. Kolonel ingin para pengungsi tak pernah tidur nyenyak.

**Soldat Jan** Itu desa, Letnan. Ada anak-anak di sana.

**Letnan de Vries** Perintah Kolonel.

Sumarno meremas cangkang keong di saku dadanya sampai terasa sakit. Baseh. Ibu. Adik.

_(Intel++: Tembakan artileri ke lereng selatan setiap fajar pukul 05.00)_

#### Ketahuan (dari menu mana pun)

Pena Jan jatuh. Ia membungkuk memungutnya, dan matanya bertemu mata Sumarno lewat celah papan.

**Soldat Jan** Letnan! Ada orang di bawah teras!

Sepatu bot menghantam papan. Sebuah tembakan menembus lantai, sejengkal dari kaki Sumarno. Ia merangkak keluar lewat sisi sungai dan terjun ke selokan, menahan napas sampai teriakan di atas sana lenyap.

_(Menyusup gagal)_

#### Mundur

Sumarno merayap mundur perlahan di sela tiang, tanpa membuat sehelai debu pun jatuh. Di atas, percakapan terus berlanjut tanpa tahu telinga mereka pernah dicuri.

### **Scene 2.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar

_(Sempurna, 5 intel)_

**Komandan Laskar** Kabel, jam jaga, radio. Kita sudah cukup untuk membuat mereka tuli dan buta sekaligus. Tapi wajahmu bukan wajah orang yang senang.

**Sumarno** Meriam itu menembak Baseh tiap fajar, Komandan. Ibu dan Adik ada di sana.

**Komandan Laskar** Besok pilihanmu, Marno. Aku tidak akan mengikatmu.

_(Cukup, 3 sampai 4 intel)_

**Komandan Laskar** Kabel dan jam jaga saja sudah sangat berharga. Kamu tahu kapan harus berhenti.

_(Minim, 1 sampai 2 intel)_

**Komandan Laskar** Satu keping lebih baik daripada nol. Besok kita tambah.

_(Gagal)_

**Komandan Laskar** Mereka tahu ada telinga di bawah teras mereka. Besok mereka lebih waspada, dan kita pun begitu.

---

## HARI 3: “Di Bawah Atap yang Runtuh” (Sulit)
### **Scene 3.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Pasukan Laskar

**Komandan Laskar** Dua karung beras dan garam untuk pejuang di pos hutan. Tiga hari mereka hanya makan daun singkong. Penjaga di jalan raya malam ini Sersan Willem. Ia tidak malas seperti Hendrik dan tidak mudah ditipu seperti Gerrit.

**Sumarno** Dan setelahnya?

**Komandan Laskar** Tempat paling berbahaya di seluruh kota: Gedung Pemerintahan. Markas Kolonel Mayer.

_(Jika Sumarno ikut Pasukan Laskar di Bab 2)_

**Sumarno** (Pelan) Gedung itu... saya yang menyalakan apinya.

**Komandan Laskar** Maka kamu tahu setiap sudutnya. Itu keuntungan kita.

_(Jika Sumarno ikut Paman di Bab 2)_

**Sumarno** Dulu saya sering lewat di depan gedung itu sepulang sekolah.

**Komandan Laskar** Kalau begitu kamu hafal lorongnya. Itu keuntungan kita.

### **Scene 3A-1** EXT. Jalan Raya Menuju Hutan - Malam
#### Misi Antar Logistik | Pemain: Sumarno, Sersan Willem

Sersan Willem berdiri tegap di tengah jalan, tidak bersandar, tidak menguap. Kepalanya bergerak cepat ke kiri dan kanan seperti burung hantu, dan ia menoleh dengan jeda yang tak bisa ditebak.

_(Willem membelakangi: tahan SPASI. Willem menoleh: lepas SPASI. Tujuh titik menuju hutan.)_

**Sumarno** (Batin) Tujuh titik. Satu langkah salah dan beras ini jadi umpan, bukan makanan.

#### Peringatan 1 (ketahuan pertama)

Senter Willem menghantam tubuh Sumarno yang terbungkuk memanggul karung.

**Willem** Berhenti! Mau ke mana?

**Sumarno** Selamatan, Tuan. Orang tua saya meninggal, ini beras untuk tahlilan.

**Willem** Di jam segini?

**Sumarno** Kami tak berani siang hari, Tuan.

Willem terdiam cukup lama.

**Willem** Jalan. Cepat.

_(Peringatan 1/2)_

#### Peringatan 2 (ketahuan kedua)

Willem mengikuti langkah Sumarno dan menusuk karung dengan ujung bayonet. Butir beras berderak jatuh.

**Willem** Selamatan sebanyak ini? Siapa yang meninggal, satu kampung?

**Sumarno** (Menahan suara agar tidak gemetar) Nenek saya, Tuan. Tamunya banyak.

**Willem** (Menatap tajam) Aku mengingat wajahmu, Nak.

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)

**Willem** Selamatan tidak membawa karung beras ke arah hutan.

Willem menarik pelatuk. Sebuah tembakan peringatan membelah kabut. Sumarno melempar karung dan melompat ke parit, berlari membungkuk di antara semak sampai suara sepatu bot memudar.

**Sumarno** (Batin, terengah) Tiga hari mereka makan daun singkong... dan aku membiarkan beras itu jatuh.

_(Logistik gagal terkirim)_

#### Berhasil

Suara burung hantu, dua pendek, satu panjang. Dari balik pepohonan muncul Pasukan Laskar, teman lama Sumarno, bersama seorang prajurit TNI berseragam compang-camping.

**Pasukan Laskar** Beras! Tiga hari kami makan daun singkong, No. Rasanya mulai seperti dendam.

**Prajurit TNI** Anak kota, hari ini kamu menghidupi satu regu.

Sumarno tersenyum lelah. Dalam hati ia teringat bubur encer di dapur umum Baseh, dan semangkuk kecil yang Adik sodorkan ke tangannya.

_(Intel++)_

_(Jika tanpa Peringatan sama sekali)_

**Prajurit TNI** Willem terkenal tak bisa dikelabui. Kamu lewat tepat di bawah hidungnya?

### **Scene 3B-1** INT. Gedung Pemerintahan, Lantai Dua - Tengah Malam
#### Misi Menyusup | Pemain: Sumarno, Kolonel Jantje Mayer, Letnan de Vries

Atap gedung itu sudah runtuh sebagian, dan bulan menyorot langsung ke meja besar berisi peta. Sumarno meringkuk di balik rangka tangga hangus, hanya selebar tangan dari kaki Kolonel Mayer. Aroma bensin lama masih melekat di kayu yang gosong.

**Kolonel Mayer** (Dingin) Dua pekan sudah. Tak satu pun pejuang tertangkap. Kota ini kuburan, tapi kuburan tidak meninggalkan jejak sepatu.

_(Intel++: Belanda mencurigai ada jaringan di dalam kota)_

_(Menu, risiko terlihat 15%: 1. Tetap, dengarkan lagi / 2. Mundur pelan-pelan)_

Sumarno menahan napas. Abu halus turun dari langit-langit dan hinggap di rambutnya.

**Kolonel Mayer** Panggil Sersan Willem. Mulai besok ia memeriksa setiap pembawa bakul dan karung di jalan raya. Tidak ada yang lewat tanpa diperiksa.

_(Intel++: Pemeriksaan ketat di jalan raya mulai besok)_

_(Menu, risiko terlihat 40%)_

Sebuah kerikil bergulir dari reruntuhan. Mayer berhenti sebentar, lalu kembali menekuni peta.

**Kolonel Mayer** (Menunjuk peta dengan tongkat) Baseh dulu. Lalu Karangnangka, Dawuhan Wetan, Windujaya. Satu desa setiap hari, sampai mereka turun sendiri.

_(Intel++: Urutan sasaran artileri, dimulai dari Baseh)_

_(Menu, risiko terlihat 65%)_

Sumarno menggenggam cangkang keong di dadanya sampai buku jarinya memutih.

**Letnan de Vries** Amunisi sitaan peninggalan Inggris dan Jepang, dua puluh lima ton, masih di gudang belakang gedung ini.

**Kolonel Mayer** Cukup untuk sebulan penuh. Tambah penjagaannya.

_(Intel++: Gudang amunisi dua puluh lima ton di belakang gedung)_

_(Menu, risiko terlihat 90%)_

Korek api menyala. Bau tembakau memenuhi ruangan. Kolonel Mayer berbicara pelan, hampir seperti bergumam pada dirinya sendiri.

**Kolonel Mayer** Seorang penjual jamu. Tiga malam berturut-turut ia mengunjungi pos-pos kita. Orang yang hanya membawa botol seharusnya tidak sering duduk dekat meja jaga.

**Letnan de Vries** Kita tangkap, Kolonel?

**Kolonel Mayer** Belum. Awasi saja. Orang seperti itu selalu membawa kita ke sarangnya.

Sumarno membeku. Ibu Jamu.

_(Intel++: Ibu Jamu sedang diawasi Belanda)_

#### Ketahuan (dari menu mana pun)

Tumit Sumarno menyenggol serpihan arang. Bunyinya kecil, tapi cukup.

**Kolonel Mayer** (Tanpa menoleh, suaranya datar) Ada tikus di bawah tangga.

**Letnan de Vries** Saya tembak, Kolonel?

**Kolonel Mayer** Tidak. Hidup-hidup. Tikus yang hidup bisa ditanyai.

Sumarno melompat dan berlari menyusuri lorong yang ia hafal di luar kepala, melewati pintu yang sudah roboh, menuruni tangga belakang, dan menghilang ke dalam kabut sementara perintah menggema di belakangnya.

_(Menyusup gagal)_

#### Mundur

Sumarno mundur selangkah demi selangkah, mengikuti bayangan reruntuhan sampai tangga belakang menelannya. Di lantai dua, Mayer masih menunduk di atas peta, tidak pernah tahu betapa dekat telinga musuh dari napasnya.

### **Scene 3.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar, Ibu Jamu

_(Sempurna, 5 intel)_

**Komandan Laskar** Dua puluh lima ton amunisi, urutan sasaran meriam, dan pemeriksaan jalan raya. Kamu membawa pulang lebih dari satu orang bisa membawa, Marno.

**Sumarno** Ada satu lagi, Komandan. Ibu Jamu sedang diawasi Kolonel Mayer.

Ibu Jamu terdiam sejenak, lalu tersenyum tipis sambil membereskan botol-botolnya.

**Ibu Jamu** Kalau begitu malam ini penjual jamu pensiun. Terima kasih sudah mengingatkan, Nak.

_(Cukup, 3 sampai 4 intel)_

**Komandan Laskar** Jalur artileri dan gudang amunisi itu sangat berarti. Berhati-hatilah, mulai besok jalan raya diperiksa lebih ketat.

_(Minim, 1 sampai 2 intel)_

**Komandan Laskar** Cukup untuk tahu mereka curiga. Dan cukup untuk tahu kita harus lebih pintar lagi.

_(Gagal)_

**Komandan Laskar** Mayer tahu ada tikus di rumahnya. Ia akan memperketat penjagaan, dan kita harus lebih berhati-hati.

**Sumarno** (Pelan, menggenggam cangkang keong) Maaf, Komandan. Marno akan lebih baik.