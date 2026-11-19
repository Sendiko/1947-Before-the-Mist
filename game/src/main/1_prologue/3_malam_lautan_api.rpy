label with_uncle:
    $ chapter_2_route = "with_uncle"
    sumarno "Maaf! Aku harus memastikan Ibu dan Adik selamat sampai posko. Pertahankan kota tercinta kita!"
    pasukan_laskar "Baiklah, No. Kamu tak perlu khawatir. Segera pergi ke posko evakuasi."
    paman "Ayo, No! Kita tidak punya banyak waktu."
    sumarno "Iya, Paman! Ibu, mari kubantu bawakan barangnya."
    ibu "Makasih ya, No."
    "Ibu mencium kening Sumarno, mengekspresikan cintanya kepada sang anak."

    sumarno "Paman, aku titip Ibu dan Adik, ya. Tolong jaga mereka sampai aku kembali."
    paman "Baiklah, No. Tepati janjimu. Awas kalau matahari terbit kamu belum sampai posko, Paman sendiri yang akan turun dan memukulimu."
    sumarno "Tenang, Paman. Aku akan tepati janjiku."
    pasukan_laskar "Ayo, No! Biar kita tidak telat. Nanti dipukuli Pamanmu, loh!"
    sumarno "Paman, Ibu, Sumarno izin pamit!"

    jump evacuation_route

label evacuation_route:
    scene black with fade
    "Jalan setapak menuju lereng dipenuhi warga yang mengungsi. Obor kecil bergoyang di tangan mereka, bayi menangis, dan roda gerobak berderit di atas tanah berbatu."
    "Sumarno berjalan paling belakang, memanggul dua buntelan. Ibu menggandeng Adik, sementara Paman memimpin rombongan."
    adik "Kak, kenapa langitnya merah? Kan ini belum pagi."
    sumarno "Itu... lampion besar, Dik. Orang-orang di kota sedang membuat lampion besar untuk menyambut kita pulang nanti."
    adik "Bohong. Lampion kok bunyinya DUAR?"
    ibu "Sudah, Dik. Jangan menoleh terus. Lihat jalan di depan, nanti kamu jatuh."
    sumarno "Paman... apa betul kota kita dibakar oleh kita sendiri?"
    paman "Betul, No. Lebih baik kota kita jadi abu di tangan sendiri daripada jadi benteng untuk Belanda."
    sumarno "Tapi itu rumah kita, Paman. Alun-alun, stasiun, pasar... semuanya."
    paman "Rumah bisa dibangun lagi, No. Tapi kalau Ibu dan Adikmu hilang, tidak ada yang bisa membangunnya kembali."
    adik "Kak, aku cuma bawa satu cangkang keong. Yang lain ketinggalan di rumah. Nanti kereta apinya jadi pendek."
    sumarno "Nanti Kakak buatkan lagi yang lebih panjang. Sama layangan juga, Kakak janji."

    "Menjelang subuh, mereka tiba di posko evakuasi di lereng Gunung Slamet."
    ibu "Minum dulu, No. Kamu dari tadi memanggul beban tidak berhenti."
    sumarno "Iya, Bu. Sebentar. Marno mau melihat ke bawah dulu."
    "Purwokerto terbentang seperti lautan api. Kobaran jingga menjilat langit dan asap hitam menggulung naik."
    sumarno "Stasiun... alun-alun... Pak Guru dulu mengajar di sebelah sana..."
    paman "Kamu lihat baik-baik, No. Ingat malam ini. Suatu hari kota itu akan kembali ke tangan kita, tapi bukan dengan tangan yang diam saja."
    sumarno "Aku akan kembali, Purwokerto."
    jump warga_melawan_penjajah_belanda


label with_laskar:
    $ chapter_2_route = "with_laskar"
    scene black with fade
    sumarno "Maafkan aku, Bu. Aku janji akan menyusul Ibu ke posko sebelum matahari terbit."
    ibu "Janji, ya, No? Ibu tunggu di posko. Jaga diri baik-baik."
    sumarno "Paman, aku titip Ibu dan Adik. Tolong jaga mereka sampai aku kembali."
    paman "Baiklah, No. Tepati janjimu."
    pasukan_laskar "Ayo, No! Biar kita tidak telat."
    sumarno "Paman, Ibu, Sumarno izin pamit!"

    "Di belakang reruntuhan gudang tua, belasan pemuda laskar berkumpul mengitari peta kasar."
    pasukan_laskar "Komandan! Ini Sumarno. Dia mau ikut."
    komandan_laskar "Umurmu berapa, Nak?"
    sumarno "Sembilan belas, Komandan!"
    komandan_laskar "Cukup. Tiga tempat harus jadi abu malam ini: Stasiun Barat, Stasiun Timur, dan Gedung Pemerintahan dekat alun-alun."
    sumarno "Siap, Komandan."
    komandan_laskar "Pastikan gedung kosong sebelum dibakar. Kita membakar bangunan, bukan menyakiti warga sendiri. Mengerti?"
    pasukan_laskar "Mengerti!"

    "Di Stasiun Barat, Sumarno dan pasukan laskar menyusup lewat pintu samping."
    pasukan_laskar "Pastikan kosong dulu, No. Cek ruang tiket, aku cek gudang."
    sumarno "Kosong?"
    pasukan_laskar "Kosong, No! Siram sekarang!"
    "Api menjalar cepat. Mereka berlari keluar dan melanjutkan perjalanan ke Stasiun Timur."
    "Di alun-alun, Gedung Pemerintahan berdiri di bawah sinar bulan."
    sumarno "Anak-anak itu mengumpulkan bambu di sini kemarin..."
    pasukan_laskar "Makanya kita lakukan ini, No. Biar bambu-bambu itu punya kota untuk dibela."
    "Sebuah ledakan mengguncang gedung. Api membubung tinggi ke langit malam."

    "Menjelang subuh, Sumarno dan kawannya meninggalkan kota."
    pasukan_laskar "No! Kamu masih ingat janjimu ke Ibumu?"
    sumarno "Astaga... iya! Posko!"
    pasukan_laskar "Cepat naik ke lereng. Biar sisanya kami urus."
    sumarno "Terima kasih, Kawan. Hati-hati!"
    "Sumarno berlari menaiki jalan setapak menuju lereng."
    "Di posko, Ibu memeluk Sumarno erat-erat. Paman dan Adik menyambutnya dengan lega."
    ibu "Alhamdulillah... Ibu kira kamu tidak jadi datang, No."
    sumarno "Marno janji, kan, Bu. Maaf Marno terlambat."
    paman "Matahari belum terbit. Hari ini kamu selamat dari Paman."
    adik "Kakak! Kakak bau asap!"
    "Dari kejauhan terdengar ledakan besar. Purwokerto terlihat seperti lautan api."
    sumarno "Purwokerto..."
    jump warga_melawan_penjajah_belanda