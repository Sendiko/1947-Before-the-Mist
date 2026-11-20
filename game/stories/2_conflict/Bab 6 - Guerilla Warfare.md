# Penyergapan: Narasi dan Dialog Gameplay
Babak 2, setelah Bab 5 (pilihan 2: Jalur Truk, Pinggir Kota)

## Catatan Desain

Setiap hari Penyergapan terdiri dari dua misi: **Sergap Penjaga** dan **Jarah Gerbong**. Kesulitan naik setiap hari. Hasil misi pertama langsung memengaruhi misi kedua.

|Hari|Tingkat|Sergap Penjaga|Jarah Gerbong|
|---|---|---|---|
|1|Mudah|2 penjaga, siluet jalan pelan, Rel Mati Pabrik Gula|5 gerbong: ransum, susu, selimut, garam, senjata|
|2|Sedang|4 penjaga, siluet lebih cepat, Emplasemen Darurat Jalan Lingkar|5 gerbong: beras, obat, kabel, peluru, senapan|
|3|Sulit|6 penjaga, siluet cepat dan rapat, Depo Lokomotif|5 gerbong: minyak, jaket, peluru, dinamit, dokumen|

Aturan yang dipakai:

- **Sergap Penjaga:** siluet penjaga berjalan melintasi layar dari arah acak (kiri ke kanan atau kanan ke kiri). Di atas kepalanya muncul lingkaran yang menyusut dari **Merah** (terlalu dini), ke **Kuning**, lalu **Hijau** (waktu terbaik). Pemain menekan SPASI untuk menyergap.
    - **Merah:** Sumarno terlalu cepat dan Pasukan Laskar turun tangan melumpuhkan penjaga. Memunculkan dialog peringatan. Penjaga ini **tidak dihitung** sebagai korban Sumarno.
    - **Kuning:** pergumulan. Setelah SPASI pertama, pemain harus menekan SPASI berkali-kali sampai bar progres penuh. Jika bar penuh, penjaga terbungkam. Jika gagal, Pasukan Laskar turun tangan dan memunculkan dialog peringatan (penjaga tidak dihitung).
    - **Hijau:** cukup satu kali tekan SPASI, penjaga terbungkam tanpa suara.
    - Cincin habis tanpa ditekan: penjaga lewat begitu saja. Tidak ada peringatan, tetapi tidak dihitung.
    - Peringatan pertama dan kedua memunculkan dialog Pasukan Laskar, **peringatan ketiga berarti gagal** (alarm berbunyi, penjaga yang tersisa tidak dikerjakan).
    - Berhasil sempurna: semua penjaga terbungkam tanpa satu pun peringatan. Memberi Semangat Juang++.
- **Jarah Gerbong:** ada 5 gerbong. Gerbong pertama gratis. Setelah itu muncul 4 menu Tetap/Mundur dengan risiko ketahuan **15%, 40%, 65%, 90%**. Setiap gerbong yang berhasil dijarah memberi Rampasan++. Menjarah kelima gerbong dihitung sempurna.
- **Pengurangan risiko:** setiap penjaga yang dibungkam Sumarno sendiri (Hijau atau Kuning berhasil) mengurangi risiko semua menu sebesar **5 poin persen**, minimal 5%. Penjaga yang dilumpuhkan Laskar (Merah atau Kuning gagal) tidak mengurangi risiko. Angka risiko yang sudah dikurangi ditampilkan di menu.
- Gagal bukan game over. Sumarno selalu lolos, tetapi rampasan hilang atau sergapan dibatalkan.
- Teks dalam _(kurung miring)_ adalah isyarat UI atau percabangan, bukan dialog.

Contoh pengurangan risiko jika semua penjaga berhasil dibungkam oleh Sumarno:

|Hari|Penjaga|Pengurangan|Risiko Menu 1 / 2 / 3 / 4|
|---|---|---|---|
|1|2|-10%|5% / 30% / 55% / 80%|
|2|4|-20%|5% / 20% / 45% / 70%|
|3|6|-30%|5% / 10% / 35% / 60%|

## HARI 1: “Rel Mati” (Mudah)
### **Scene 1.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Pasukan Laskar

Komandan Laskar membentangkan peta karung di atas mesin penggiling. Ujung rantingnya berhenti di sebuah garis hitam di pinggir kota, bekas rel cabang Pabrik Gula.

**Komandan Laskar** Belanda memarkir lima gerbong di rel mati ini. Menunggu truk dari pos pasar untuk mengangkutnya. Penjaganya cuma dua, dan mereka bosan.

**Pasukan Laskar** Aku yang menemanimu malam ini, No. Kita kerjakan dalam dua tahap. Sunyikan dulu penjaganya, baru jarah gerbongnya.

Komandan menyodorkan sebilah belati bersarung kain. Sumarno menerimanya dengan kedua tangan, tapi tidak langsung menggenggam gagangnya.

**Sumarno** (Pelan) Saya belum pernah...

**Komandan Laskar** Tidak ada yang pernah, Marno. Dan tidak ada yang siap. Kita tidak merayakan ini. Kita menyelesaikannya.

**Komandan Laskar** Ingat satu hal. Semakin sedikit penjaga yang berdiri, semakin sedikit mata yang melihatmu di gerbong. Kerjakan yang pertama dengan baik, yang kedua jadi lebih mudah.

Sumarno menyelipkan belati ke ikat pinggangnya. Tangannya yang lain menyentuh cangkang keong di saku dada.

**Sumarno** (Batin) Janji yang bisa kamu tepati saja, No.

### **Scene 1A-1** EXT. Rel Mati, Bekas Pabrik Gula - Malam
#### Misi Sergap Penjaga | Pemain: Sumarno, Pasukan Laskar

Kabut menggantung rendah di antara rangka pabrik yang hangus. Dari balik tumpukan bantalan rel, Sumarno dan temannya mengintip. Dua siluet penjaga berjalan bergantian di sepanjang rel, senapan tersampir malas.

_(Siluet penjaga melintas dari kiri atau kanan secara acak. Lingkaran menyusut di atas kepalanya: Merah, Kuning, Hijau. Tekan SPASI. Total 2 penjaga.)_

**Pasukan Laskar** (Berbisik) Tunggu sampai ia lewat di depan kita. Jangan bergerak waktu cincinnya masih merah.

**Sumarno** (Batin) Seperti menunggu angin untuk layangan Adik. Terlalu cepat, jatuh. Terlalu lambat, putus.

#### Hijau (satu tekan)
Sumarno melangkah tepat di belakang bayangan itu. Satu gerakan, satu tangan membekap, satu tarikan napas. Tubuh itu merosot pelan ke tanah tanpa suara. Sumarno memejamkan mata sejenak, lalu menariknya ke balik bantalan rel.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Kuning berhasil (bar progres penuh)
Penjaga itu sempat menyikut perutnya. Sumarno menggertakkan gigi, mengunci leher lawannya dengan seluruh tenaganya sampai perlawanan itu mereda. Napasnya terengah, kedua tangannya gemetar.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Peringatan 1 (Merah, atau Kuning gagal)
Sumarno melompat terlalu cepat, penjaga itu berbalik dan hampir berteriak. Dari kegelapan, Pasukan Laskar menerjang dan membekap mulutnya sampai tubuh itu lemas.

**Pasukan Laskar** (Berbisik, tajam) Tunggu cincinnya hijau, No! Kali ini aku bantu. Jangan ulangi.

_(Peringatan 1/2)_

#### Peringatan 2 (Merah, atau Kuning gagal)
Lagi-lagi Sumarno bergerak sebelum waktunya. Penjaga itu terhuyung dan menarik napas untuk berteriak. Pasukan Laskar sekali lagi muncul di belakangnya.

**Pasukan Laskar** (Berbisik, rahangnya mengeras) Dua kali, No. Kalau terjadi sekali lagi, kita mundur. Aku tidak mau mati di rel ini.

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)
Penjaga itu berteriak sebelum tangan siapa pun sempat membungkamnya.

**Soldat Dirk** Alarm! Ada orang di rel!

Peluit meraung. Senapan dikokang. Pasukan Laskar menarik lengan Sumarno dan menyeretnya ke dalam kabut. Mereka berlari di antara reruntuhan pabrik sampai suara sepatu bot menjauh.

**Pasukan Laskar** (Terengah) Gerbong itu tidak mungkin kita sentuh malam ini. Bagaimana, No?

**Sumarno** (Batin) Marno terlalu terburu-buru...

_(Sergap gagal. Penjaga yang dibungkam sebelum kegagalan tetap dihitung. Lanjut ke Scene 1B-1 dengan teks varian "waspada")_

#### Berhasil (semua penjaga selesai
Kedua siluet sudah tidak ada. Rel mati itu hening, hanya terdengar embusan angin di antara besi hangus. Lima gerbong berdiri berjajar dalam kabut, bagai barisan hantu.

**Pasukan Laskar** (Menepuk bahu Sumarno) Bagus, No. Sekarang giliran gerbongnya.

_(Jika tanpa Peringatan sama sekali)_

**Pasukan Laskar** Tanpa satu pun kesalahan? Hari pertama? Aku mulai takut padamu, No.

### **Scene 1B-1** EXT. Gerbong Kereta, Rel Mati - Tengah Malam
#### Misi Jarah Gerbong | Pemain: Sumarno, Pasukan Laskar

Sumarno memanjat ke atas gerbong pertama. Pasukan Laskar berjaga di bawah, mengawasi kabut. Gerbong kayu itu berbau besi dan debu arang.

_(Jika Sergap gagal: Dari kejauhan masih terdengar peluit dan langkah sepatu bot yang berkeliling. Sumarno bergerak lebih berhati-hati.)_

_(Gerbong 1, gratis. Menjarah otomatis berhasil.)_

Gerbong pertama berisi tumpukan batubara. Sumarno terdiam. Cangkang keong, kereta api, gerbong batubara. Ia hampir tersenyum. Di bawah batu hitam itu, terselip berpeti-peti ransum biskuit.

**Sumarno** (Batin) Seandainya Adik melihat ini. Gerbong batubaranya akhirnya ada isinya.

_(Semangat Juang++: Ransum biskuit)_

_(Menu, risiko terlihat 15%: 1. Tetap, jarah gerbong berikutnya / 2. Mundur pelan-pelan)_

Gerbong kedua berderit ketika pintunya digeser. Di dalamnya, kaleng-kaleng susu dan sarden tersusun rapi. Tidak ada yang menoleh.

**Pasukan Laskar** (Berbisik dari bawah) Cepat, No. Jangan serakah di satu tempat.

_(Rampasan++: Kaleng susu dan sarden)_

_(Menu, risiko terlihat 40%)_

Di gerbong ketiga, Sumarno menemukan gulungan selimut wol. Ia mengusap bahannya, teringat para pengungsi yang menggigil di bawah tenda terpal Baseh.

_(Semangat Juang++: Selimut wol)_

_(Menu, risiko terlihat 65%)_

Gerbong keempat lebih sempit. Karung garam dan gula merah ditumpuk sampai atap. Sebatang bambu bergeser di bawah kakinya, berderak pelan.

**Sumarno** (Batin) Jangan sekarang. Jangan sekarang.

_(Semangat Juang++: Garam dan gula)_

_(Menu, risiko terlihat 90%)_

Gerbong kelima dikunci dengan gembok besar. Sumarno mengganjal pengungkit di antara palang dan menekannya perlahan, menahan bunyi. Gembok itu terlepas. Di dalam, peti-peti kayu bertuliskan huruf asing berjajar rapat. Satu peti terbuka sedikit, menampakkan kilau laras senapan.

**Sumarno** (Batin, nyaris tak bersuara) Dua penjaga untuk ini? Mereka benar-benar remeh pada kita.

_(Semangat Juang++: Peti senapan dan amunisi)_

#### Ketahuan (dari menu mana pun)
Sebuah peti terlepas dari tumpukan dan menghantam lantai gerbong. Bunyinya seperti dentuman.

**Soldat Bram** (Dari kejauhan) Wie is daar? Siapa di sana?

_(Jika masih ada penjaga yang tidak dibungkam)_ Senter menyapu rel. Pasukan Laskar menarik Sumarno turun dan keduanya berlari menyusuri parit.

_(Jika semua penjaga dibungkam)_ Truk patroli yang baru datang menyoroti rel dengan lampu depannya. Pasukan Laskar menarik Sumarno turun dan keduanya berlari menyusuri parit.

Sumarno tiba di markas dengan tangan kosong dan jantung berdentum.

_(Jarah gagal. Rampasan hilang)_

#### Mundur
**Sumarno** (Batin) Cukup. Yang sudah di tangan lebih baik daripada yang masih di gerbong.

Ia melompat turun dan memberi isyarat. Keduanya memanggul hasil rampasan dan menghilang bersama kabut sebelum truk pengangkut tiba.

### **Scene 1.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar

_(Sempurna, 5 gerbong)_

**Komandan Laskar** Lima gerbong, tak satu pun tersisa. Truk mereka besok akan mengangkut angin.

**Sumarno** (Menunduk) Tapi dua orang itu, Komandan...

**Komandan Laskar** Aku tahu, Marno. Besok malam, jumlahnya lebih banyak. Kamu boleh membenci ini. Jangan sampai kamu terbiasa.

_(Cukup, 3 sampai 4 gerbong)_

**Komandan Laskar** Cukup. Tahu kapan berhenti adalah bagian dari bertarung.

_(Minim, 1 sampai 2 gerbong)_

**Komandan Laskar** Sedikit, tapi cukup untuk makan beberapa hari. Yang serakah biasanya tidak pulang.

_(Gagal)_

**Komandan Laskar** Kamu hidup, itu yang terpenting. Besok kita coba lagi.

**Sumarno** (Menunduk) Maaf, Komandan.

---

## HARI 2: “Cahaya Senter” (Sedang)
### **Scene 2.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Pasukan Laskar

**Komandan Laskar** Malam ini Emplasemen Darurat di Jalan Lingkar Timur. Lima gerbong baru dari pelabuhan utara, empat penjaga, dan semuanya membawa senter.

**Pasukan Laskar** Mereka jalan lebih cepat dan lebih rapat. Kalau salah menghitung, kita dikepung dari dua sisi.

**Sumarno** Dan gerbongnya, Komandan?

**Komandan Laskar** Obat, kabel, peluru. Kita butuh semuanya. Empat penjaga, empat kali kesempatan. Gunakan dengan benar.

_(Jika pemain sudah menyelesaikan Telik Sandi Hari 2 dan mendapat intel "Satu-satunya kabel telepon militer lewat tiang jalan lingkar")_

**Sumarno** Kabel di jalan lingkar itu, Komandan. Satu-satunya jalur telepon mereka ke Banyumas.

**Komandan Laskar** Dan sekarang kita punya kesempatan mencuri gulungan cadangannya. Tanpa cadangan, kalau kabel itu putus, mereka tuli.

### **Scene 2A-1** EXT. Emplasemen Darurat, Jalan Lingkar Timur - Malam
#### Misi Sergap Penjaga | Pemain: Sumarno, Pasukan Laskar, Prajurit TNI

Kabut lebih tipis dari semalam. Empat siluet berjalan bolak-balik di antara gerbong, cahaya senter menyapu ke segala arah. Jarak antar penjaga lebih rapat, dan langkah mereka lebih cepat.

_(Total 4 penjaga. Lingkaran menyusut lebih cepat dari Hari 1.)_

**Pasukan Laskar** (Berbisik) Dengar baik-baik. Mereka tidak akan memberi kita waktu panjang. Perhatikan cincinnya.

**Sumarno** (Batin) Empat. Aku tidak mau menghitungnya, tapi aku harus.

#### Hijau (satu tekan)
Cahaya senter bergeser ke kiri. Sumarno menyelinap dari kanan, membekap, dan menahan tubuh itu agar senter di tangannya tidak jatuh menghantam batu.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Kuning berhasil (bar progres penuh)
Penjaga itu melawan lebih keras dari yang Sumarno bayangkan. Senter terlempar dan berguling, cahayanya berputar liar. Sumarno menahan sampai semuanya berhenti. Prajurit TNI menyambar senter dan mematikannya sebelum ada yang sempat menoleh.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Peringatan 1 (Merah, atau Kuning gagal)
Penjaga itu berbalik tepat saat Sumarno menerjang. Prajurit TNI dan Pasukan Laskar menyergap dari dua sisi dan membungkamnya sebelum sempat berteriak.

**Pasukan Laskar** (Berbisik) Sabar, Nak. Tunggu waktunya. Jangan sampai kita yang membayar kesalahanmu.

_(Peringatan 1/2)_

#### Peringatan 2 (Merah, atau Kuning gagal)

Senter berputar ke arah semak tempat mereka bersembunyi. Pasukan Laskar menarik Sumarno merunduk, sementara Prajurit TNI menyelesaikan tugas yang gagal dikerjakan.

**Pasukan Laskar** (Berbisik) Kamu terlalu gugup, No. Tarik napas. Satu kali lagi, dan senter itu menemukan kita.

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)

**Kopral Maarten** (Berteriak) Hij is hier! Mereka di sini!

Senter menyorot ke segala arah. Tembakan pertama pecah di udara. Prajurit TNI menarik Sumarno, dan mereka berlari menembus kabut menuju parit.

**Pasukan Laskar** (Terengah) Gerbong itu hilang malam ini. Pulang.

_(Sergap gagal. Penjaga yang dibungkam sebelum kegagalan tetap dihitung. Lanjut ke Scene 2B-1 dengan teks varian "waspada")_

#### Berhasil (semua penjaga selesai)
Satu per satu senter padam. Emplasemen itu kembali gelap, hanya diterangi pantulan bulan di atas rel.

**Pasukan Laskar** (Menghela napas) Empat. Bersih. Kamu tumbuh cepat, Nak.

_(Jika tanpa Peringatan sama sekali)_

**Pasukan Laskar** Tidak ada satu pun senter yang jatuh ke arahmu? Ajari aku cara bernapas seperti itu.

### **Scene 2B-1** EXT. Gerbong Kereta, Emplasemen Darurat - Tengah Malam
#### Misi Jarah Gerbong | Pemain: Sumarno, Pasukan Laskar

Gerbong-gerbong baru itu masih berbau cat. Sumarno memanjat gerbong pertama sementara Prajurit TNI berjaga di ujung rel.

_(Jika Sergap gagal: Dari kejauhan terdengar suara anjing pelacak. Sumarno harus bergerak cepat.)_

_(Gerbong 1, gratis. Menjarah otomatis berhasil.)_

Karung beras dan garam menumpuk sampai atap. Sumarno menarik napas lega.

_(Rampasan++: Beras dan garam)_

_(Menu, risiko terlihat 15%: 1. Tetap, jarah gerbong berikutnya / 2. Mundur pelan-pelan)_

Gerbong kedua penuh peti kayu bergambar palang merah. Perban, kina, dan botol-botol kecil berjajar rapi. Sumarno teringat laskar yang terluka di surau tua.

**Pasukan Laskar** (Berbisik) Jangan terlalu lama melamun, No.

_(Rampasan++: Obat dan perban)_

_(Menu, risiko terlihat 40%)_

Gerbong ketiga menyimpan gulungan kabel telepon militer dan peralatan penyambung. Sumarno menggulungnya perlahan agar tidak berbunyi.

**Sumarno** (Batin) Kalau ini hilang, mereka tidak bisa menyambung yang putus.

_(Rampasan++: Kabel telepon dan peralatan sambung)_

_(Menu, risiko terlihat 65%)_

Pintu gerbong keempat tersangkut. Sumarno menggesernya sedikit demi sedikit, menahan bunyi besi yang bergesek. Di dalamnya, peti-peti peluru karabin tersusun rapi.

_(Rampasan++: Peluru karabin)_

_(Menu, risiko terlihat 90%)_

Gerbong kelima memiliki dua lapis kunci. Sumarno menekan pengungkit sampai tangannya gemetar. Kunci pertama terbuka, lalu kedua. Di dalamnya, peti-peti senapan tersusun bagai tulang rusuk raksasa.

**Pasukan Laskar** (Berbisik dari bawah, nyaris tak percaya) Pakai tanganmu sendiri, No. Jangan tunggu aku.

_(Rampasan++: Peti senapan)_

#### Ketahuan (dari menu mana pun)

Pintu gerbong menghantam rangka besi dengan suara menggema. Senter menyapu dari kejauhan.

**Kopral Maarten** (Dari kejauhan) Siapa itu? Berhenti!

Sumarno meloncat turun dan berlari bersama Pasukan Laskar, melewati parit, melewati tiang telepon, dan menghilang ke dalam kabut.

_(Jarah gagal. Rampasan hilang)_

#### Mundur

Sumarno melompat turun dengan hati-hati. Pasukan Laskar memanggul hasil jarahan, dan mereka berdua menghilang di antara rel sebelum senter berikutnya datang.

### **Scene 2.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar, Prajurit TNI

_(Sempurna, 5 gerbong)_

**Komandan Laskar** Beras, obat, kabel, peluru, senapan. Satu gerbong lagi, dan aku mulai curiga kamu mencuri dari kantor Kolonel.

**Sumarno** (Pelan) Mereka akan menembaki Baseh setiap fajar, Komandan. Setiap peluru yang kita curi, satu peluru yang tidak sampai ke sana.

**Komandan Laskar** Itu alasan yang baik untuk bertarung, Marno.

_(Cukup, 3 sampai 4 gerbong)_

**Komandan Laskar** Obat dan kabel sudah cukup banyak. Pasukan kita bisa bernapas.

_(Minim, 1 sampai 2 gerbong)_

**Komandan Laskar** Sedikit, tapi cukup untuk beberapa orang bertahan. Besok kita tambah.

_(Gagal)_

**Komandan Laskar** Mereka tahu ada orang di rel. Besok mereka lebih waspada, dan kita pun begitu.

---

## HARI 3: “Depo Lokomotif” (Sulit)
### **Scene 3.0** INT. Markas, Bekas Penggilingan Padi - Malam
#### Pemain: Sumarno, Komandan Laskar, Pasukan Laskar

**Komandan Laskar** Depo Lokomotif tua di ujung kota. Kolonel Mayer menyimpan lima gerbong terakhirnya di sana, dengan enam penjaga yang mereka sebut "terbaik".

**Pasukan Laskar** Mereka tidak seceroboh dua malam sebelumnya. Mereka berjalan rapat dan menoleh bergantian.

**Sumarno** Dan isinya?

**Komandan Laskar** Dinamit, peluru, dan sesuatu yang disebut Kolonel sebagai "dokumen penting". Dua gerbong pertama akan membantu kita bertahan, dua berikutnya mempersiapkan kita menyerang, dan yang terakhir bisa mengubah segalanya.

_(Jika Sumarno ikut Pasukan Laskar di Bab 2)_

**Sumarno** (Pelan) Saya yang dulu membakar stasiun itu. Sekarang saya harus mencuri dari sisa-sisanya.

**Komandan Laskar** Dan kamu tahu setiap sudutnya. Itu keuntungan kita.

_(Jika Sumarno ikut Paman di Bab 2)_

**Sumarno** Dulu saya sering melihat kereta berhenti di sana, sepulang sekolah.

**Komandan Laskar** Kalau begitu kamu hafal sudutnya. Itu keuntungan kita.

### **Scene 3A-1** EXT. Depo Lokomotif Tua - Malam

#### Misi Sergap Penjaga | Pemain: Sumarno, Pasukan Laskar, Prajurit TNI

Atap seng depo itu berderak ditiup angin. Enam siluet berjalan dengan jarak rapat, bergantian menyapukan senter dari kiri ke kanan. Tidak ada celah yang jelas.

_(Total 6 penjaga. Lingkaran menyusut paling cepat. Siluet lebih sering bersilangan.)_

**Pasukan Laskar** (Berbisik) Ini yang paling sulit, Nak. Kalau salah, kita tidak akan sempat mundur.

**Sumarno** (Batin) Enam. Ya Allah, kuatkan tanganku. Dan maafkan aku.

#### Hijau (satu tekan)
Sumarno menunggu sampai cahaya senter benar-benar membelakanginya. Satu langkah, satu gerakan. Penjaga itu jatuh tanpa suara.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Kuning berhasil (bar progres penuh)
Tubuh Sumarno menegang. Penjaga itu mencengkeram lengannya, tapi akhirnya terkulai juga. Sumarno bersandar pada dinding, menahan napas yang tersengal.

_(Penjaga terbungkam. Risiko jarah -5%)_

#### Peringatan 1 (Merah, atau Kuning gagal)
Penjaga itu menoleh seketika. Prajurit TNI menjatuhkannya sebelum ia sempat membuka mulut.

**Prajurit TNI** (Berbisik, dingin) Tidak ada kesempatan kedua di tempat ini. Tunggu hijau.

_(Peringatan 1/2)_

#### Peringatan 2 (Merah, atau Kuning gagal)

Dua senter bertemu di tempat Sumarno bersembunyi. Pasukan Laskar menarik tubuhnya ke belakang tiang, sementara Prajurit TNI menyelesaikan tugasnya dalam hitungan detik.

**Pasukan Laskar** (Berbisik, gemetar) Kalau begini terus kita mati semua, No!

_(Peringatan 2/2. Satu kesalahan lagi berarti gagal.)_

#### Gagal (ketahuan ketiga)
Sebuah teriakan membelah malam.

**Soldat** Alarm! Alarm! Ada penyusup di depo!

Peluit meraung dari segala arah. Tembakan menghantam seng atap. Prajurit TNI menarik Sumarno, dan ketiganya berlari menyusuri rel sampai suara-suara itu mengecil.

**Prajurit TNI** (Terengah) Mereka tahu kita di sini. Pulang, sekarang.

_(Sergap gagal. Penjaga yang dibungkam sebelum kegagalan tetap dihitung. Lanjut ke Scene 3B-1 dengan teks varian "waspada")_

#### Berhasil (semua penjaga selesai)
Depo itu sunyi. Enam senter padam di enam tempat berbeda. Sumarno berdiri terpaku, menatap telapak tangannya yang gemetar dalam cahaya bulan.

**Sumarno** (Batin, nyaris tak terdengar) Enam. Mereka juga punya ibu.

Prajurit TNI menepuk bahunya tanpa berkata apa-apa.

_(Jika tanpa Peringatan sama sekali)_

**Prajurit TNI** Tanpa satu kesalahan melawan enam penjaga terbaik? Kalau semua anak muda sepertimu, Belanda sudah lama pulang.

### **Scene 3B-1** EXT. Gerbong Kereta, Depo Lokomotif - Tengah Malam
#### Misi Jarah Gerbong | Pemain: Sumarno, Pasukan Laskar, Prajurit TNI

Lima gerbong berdiri di bawah atap depo yang setengah runtuh. Sumarno memanjat gerbong pertama dengan hati-hati. Debu arang menempel di tangannya.

_(Jika Sergap gagal: Alarm masih meraung dari kejauhan. Setiap langkah Sumarno terasa seperti hitungan mundur.)_

_(Gerbong 1, gratis. Menjarah otomatis berhasil.)_

Gerbong pertama dipenuhi jerigen minyak tanah. Sumarno mengangkat satu, mengendusnya, dan menahan bau yang mengingatkannya pada malam di stasiun.

_(Rampasan++: Minyak tanah)_

_(Menu, risiko terlihat 15%: 1. Tetap, jarah gerbong berikutnya / 2. Mundur pelan-pelan)_

Gerbong kedua menyimpan jaket kulit dan sepatu bot. Sumarno memikirkan para pejuang di hutan yang bertelanjang kaki.

_(Rampasan++: Jaket dan sepatu)_

_(Menu, risiko terlihat 40%)_

Di gerbong ketiga, peti-peti peluru tersusun sampai atap. Debu dari peti itu membuat Sumarno hampir bersin. Ia menahannya, mata berair.

**Pasukan Laskar** (Berbisik dari bawah) Jangan sekarang, Nak. Tahan.

_(Rampasan++: Peluru)_

_(Menu, risiko terlihat 65%)_

Gerbong keempat dikunci dari luar dengan rantai. Sumarno memotongnya perlahan dengan gunting besi. Di dalamnya, peti kayu bertuliskan peringatan dalam huruf merah: dinamit.

**Sumarno** (Batin) Cukup untuk meledakkan satu rel kereta. Atau satu jembatan.

_(Rampasan++: Dinamit)_

_(Menu, risiko terlihat 90%)_

Gerbong kelima adalah gerbong baja berpintu tebal. Sumarno meraba engselnya dan menemukan sebuah celah. Di dalamnya terdapat peti baja kecil berisi tumpukan dokumen bersampul merah. Ia membuka satu lembar. Peta, daftar pos jaga, jadwal konvoi, dan sandi radio.

**Sumarno** (Batin, terkejut) Ini bukan sekadar rampasan. Ini peta mereka.

_(Rampasan++: Dokumen dan sandi militer Belanda)_

#### Ketahuan (dari menu mana pun)
Sebuah jerigen terlepas dari genggamannya dan menghantam lantai baja. Gaungnya memenuhi depo.

**Soldat** Siapa itu?! Cari ke seluruh gerbong!

Senter dan suara sepatu bot datang dari semua arah. Sumarno melompat dari pintu belakang, menembus lorong yang ia hafal di luar kepala, dan menghilang ke dalam kabut sementara perintah menggema di belakangnya.

_(Jarah gagal. Rampasan hilang)_

#### Mundur
Sumarno mundur selangkah demi selangkah, mengikuti bayangan tiang. Prajurit TNI dan Pasukan Laskar menunggunya di pintu belakang, memanggul hasil jarahan yang sudah mereka kumpulkan.

### **Scene 3.9** INT. Markas - Menjelang Subuh
#### Laporan | Pemain: Sumarno, Komandan Laskar, Prajurit TNI

_(Sempurna, 5 gerbong)_

**Komandan Laskar** Minyak, jaket, peluru, dinamit, dan dokumen mereka. Kolonel Mayer akan bangun besok pagi dan mendapati depo kosong.

**Pasukan Laskar** Dan dengan dinamit dan peta itu, Komandan, kita bisa mulai bicara soal rel mereka.

**Sumarno** (Pelan) Enam penjaga, Komandan. Saya tidak ingin ini menjadi mudah.

**Komandan Laskar** Tidak akan, Marno. Dan jangan sampai.

_(Cukup, 3 sampai 4 gerbong)_

**Komandan Laskar** Dinamit saja sudah cukup berharga. Kamu tahu kapan harus berhenti, Marno.

_(Minim, 1 sampai 2 gerbong)_

**Komandan Laskar** Sedikit, tapi benar. Cukup untuk tahu mereka menyembunyikan sesuatu di depo itu.

_(Gagal)_

**Komandan Laskar** Mayer akan memperketat depo itu, dan kita harus lebih berhati-hati.

**Sumarno** (Pelan, menggenggam cangkang keong) Maaf, Komandan. Marno akan lebih baik.