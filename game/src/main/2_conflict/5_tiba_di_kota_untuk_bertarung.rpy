default chapter_5_choice = None

label tiba_di_kota_untuk_bertarung:
    scene black with fade
    "Kabut begitu pekat hingga obor pun tak berguna. Paman berjalan di depan tanpa penerangan, menyibak semak dengan tongkat bambu."
    "Sumarno mengikuti tepat di belakangnya, satu tangan menekan cangkang keong di saku dada agar tidak berbunyi."
    "Dari kejauhan terdengar deru mesin truk, lalu suara orang berteriak dalam bahasa yang tidak ia mengerti."
    "Paman mengangkat tangan. Keduanya membeku di balik rumpun bambu."
    paman "(Berbisik) Dengar baik-baik, No. Patroli mereka lewat tiap seperempat malam. Bukan jam, tapi kebiasaan. Mereka malas turun dari truk kalau kabut setebal ini."
    sumarno "(Berbisik) Paman tahu dari mana?"
    paman "Dari tiga hari memperhatikan, sambil pura-pura jual singkong."
    "Sumarno hampir tertawa, tapi tertahan. Mereka kembali melangkah, lebih pelan, menyusuri parit kering di belakang deretan rumah yang gelap dan kosong."
    "Pintu-pintu terbuka. Sebuah kursi rotan tergeletak di tengah jalan."
    "Sumarno memperlambat langkah di depan sebuah rumah dengan pagar kayu yang ia kenal."
    sumarno "Ini rumah Pak Guru..."
    paman "Jangan dilihat, No. Kalau dilihat, kaki jadi berat."
    "Sumarno memaksa matanya lurus ke depan."
    "Di ujung parit berdiri sebuah bangunan tua berdinding seng berkarat, bekas penggilingan padi, setengah tertutup rimbun bambu."
    "Paman berhenti sepuluh langkah darinya, menyatukan kedua telapak tangan di depan mulut, dan menirukan suara burung hantu dua kali pendek, satu kali panjang."
    "Hening. Lalu dari balik bangunan, terdengar balasan yang sama."
    paman "Kita sampai. Dengar, di dalam sana ada orang yang kenal Paman, ada yang tidak. Jangan banyak bicara sebelum ditanya."
    sumarno "Iya, Paman."
    paman "Dan No..."
    "Paman menatapnya sebentar. Untuk pertama kalinya, sorot matanya tidak terlihat seperti seorang paman, tapi seperti seorang prajurit."
    paman "Mulai malam ini kamu bukan cuma keponakan Paman."

    scene black with dissolve
    "Di dalam, satu lampu minyak berselubung kain hitam menjadi satu-satunya cahaya. Mesin penggiling tua berdiri dalam bayang-bayang seperti raksasa tertidur."
    "Belasan orang duduk melingkar: laskar muda berbaju lusuh, dua prajurit TNI dengan seragam compang-camping, seorang pedagang tahu, seorang tukang becak, dan seorang ibu penjual jamu yang duduk paling dekat dengan peta."
    "Semua kepala menoleh ketika Sumarno dan Paman melangkah masuk."
    "Dari sudut ruangan, seorang pemuda berdiri dengan wajah penuh lega. Teman Sumarno dari barisan laskar."
    pasukan_laskar "No! Alhamdulillah kamu masih utuh! Aku kira api semalam sudah melahapmu!"
    sumarno "(Tersenyum lelah) Belum jodoh, Kawan."
    "Komandan Laskar bangkit dari tempat duduknya. Ia mengamati Sumarno beberapa saat, lalu menoleh pada Paman."
    komandan_laskar "Ini keponakan yang Anda ceritakan?"
    paman "Ya. Keras kepala, tapi hafal setiap gang di kota ini."

    if chapter_2_route == "with_laskar":
        komandan_laskar "Sembilan belas tahun, katamu semalam."
        "Sumarno menunduk."
        komandan_laskar "Saya sudah tahu itu bohong sejak kamu menjawab terlalu cepat. Tapi api di stasiun dan alun-alun tidak bohong. Bohongmu saya maafkan."
        "Paman melirik Sumarno dengan alis terangkat. Sumarno hanya bisa meringis."
    else:
        komandan_laskar "Umurmu berapa, Nak?"
        sumarno "Sembilan belas, Komandan."
        komandan_laskar "Jujur. Itu lebih berguna dari keberanian palsu."

    "Komandan mengangguk ke arah lingkaran. Sumarno duduk di antara mereka."
    "Di tengah, terbentang peta kota yang digambar tangan di atas lembaran karung. Beberapa titik ditandai dengan arang."
    "Pasukan Belanda sudah mengubah pasar menjadi pos jaga, dan alun-alun menjadi tempat parkir truk."
    komandan_laskar "Kita tidak punya meriam, tidak punya tank, dan jumlah kita sedikit. Yang kita punya adalah kabut, rasa kenal pada tanah ini, dan warga yang tidak mau menyerah. Itu cukup, asal dipakai dengan benar."
    "Ia menyentuh peta dengan ujung ranting."
    komandan_laskar "Ibu Jamu ini sudah dua hari keliling menjual jamu ke tentara Belanda. Mereka bicara banyak kalau perutnya hangat."
    ibu_jamu "(Tersenyum kecil) Orang yang dikira cuma pembawa botol itu jarang dicurigai, Nak."
    tukang_becak "Saya juga punya cerita soal jalur truk mereka dari pelabuhan utara. Hanya saja saya butuh orang yang berani mencatat."
    "Sumarno menatap wajah-wajah di sekelilingnya. Orang biasa yang tiba-tiba memikul sesuatu yang jauh lebih besar dari diri mereka."
    pasukan_laskar "Pak Komandan, kasih tahu dia soal tugas-tugasnya."
    komandan_laskar "Malam ini kita tidak menyerang. Malam ini kita belajar membaca kota yang sudah berubah. Tapi mulai besok kita punya tiga pekerjaan, dan tidak semuanya bisa dikerjakan satu orang dalam satu malam."
    "Ia mengangkat tiga jari."
    komandan_laskar "Pertama, mata. Kita harus tahu setiap patroli, setiap pos, setiap percakapan yang bisa kita curi. Tanpa itu, kita buta."
    komandan_laskar "Kedua, taring. Truk logistik dan patroli kecil yang berjalan terpisah. Kabut ini milik kita, dan kita harus belajar menyergap tanpa bunyi."
    komandan_laskar "Ketiga, rumah. Desa-desa di lereng sudah mulai ditembaki. Pejuang yang bertarung sambil memikirkan keluarganya yang kelaparan tidak akan bertahan lama."
    "Sumarno menegang. Wajah Ibu dan Adik terlintas di benaknya."
    paman "(Pelan, hanya terdengar oleh Sumarno) Paman akan naik lagi ke Baseh sebelum subuh. Jalur tikus itu hanya Paman yang hafal. Kalau kamu mau ikut menjaga mereka, ikut Paman. Kalau kamu mau di kota, Paman akan sampaikan salammu."
    sumarno "..."
    komandan_laskar "Kamu yang memilih, Marno. Tidak ada pilihan yang salah. Tapi semuanya punya harga."
    "Sumarno menarik napas panjang. Peta kasar di hadapannya seolah hidup, tiga titik terang di antara arang dan kabut."

    scene black with dissolve
    "Layar beralih ke peta dari atas, digambar tangan di atas karung. Kabut tipis bergerak pelan di atasnya. Tiga titik menyala bergantian."

    menu:
        "Jalan-jalan Kota (Telik Sandi)":
            $ chapter_5_choice = "telik_sandi"
        "Jalur Truk, Pinggir Kota (Penyergapan)":
            $ chapter_5_choice = "penyergapan"
        "Lereng Gunung Slamet, Baseh (Lindungi Keluarga)":
            $ chapter_5_choice = "lindungi_keluarga"

    return
