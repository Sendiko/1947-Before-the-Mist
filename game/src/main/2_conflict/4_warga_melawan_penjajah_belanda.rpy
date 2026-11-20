default chapter_2_route = "unknown"

label warga_melawan_penjajah_belanda:
    scene black with fade
    "Matahari terbit di balik kabut tebal. Asap hitam dari kota masih terlihat di kejauhan, tipis dan menggantung seperti kain lusuh."
    "Di dapur umum, para ibu membagikan bubur encer. Tidak ada yang berbicara banyak."

    adik "Kak, makan. Kata Ibu kalau tidak makan nanti sakit."
    sumarno "(Tersenyum tipis) Iya, Dik. Terima kasih."
    "Adik duduk di sampingnya, menyusun cangkang keong di atas tanah. Hanya ada satu cangkang, jadi kereta apinya tidak bisa bergerak."
    adik "Kak, kita pulang kapan?"
    sumarno "Nanti, Dik. Kalau semuanya sudah aman."

    if chapter_2_route == "with_uncle":
        "Tangannya mengepal di atas lutut. Ia selamat, tapi teman-temannya mungkin masih di sana. Rasa bersalah itu belum pergi."
    elif chapter_2_route == "with_laskar":
        "Ia menatap telapak tangannya yang masih menghitam oleh jelaga. Bau bensin belum hilang meski sudah dicuci. Ia tidak berani menatap Ibu terlalu lama."

    paman "Semua kumpul! Ada kabar dari bawah!"

    scene black with dissolve
    "Iring-iringan truk dan jip Belanda memasuki alun-alun Purwokerto. Tidak ada sambutan, tidak ada perlawanan. Yang ada hanya puing hitam, bau hangus, dan asap yang masih mengepul dari Gedung Pemerintahan."
    "Kolonel Jantje Mayer turun dari jipnya. Sepatu botnya menginjak abu. Ia menatap sekeliling tanpa ekspresi."
    tentara_belanda "Kolonel, stasiun, jembatan, dan gedung pemerintahan semuanya hancur. Tidak ada yang bisa dipakai."
    kolonel_mayer "(Pelan, dingin) Mereka tidak meninggalkan kita kota. Mereka meninggalkan kita kuburan."
    "Ia mengambil sepotong bambu runcing yang hangus dari tanah, memutarnya di tangan, lalu mematahkannya."
    kolonel_mayer "Orang-orang yang membakar kota ini belum jauh. Geledah setiap rumah. Setiap sumur. Setiap lumbung. Saya mau mereka ditemukan sebelum malam."
    tentara_belanda "Dan para pengungsi di lereng gunung, Kolonel?"
    "Mayer menoleh ke arah Gunung Slamet yang tertutup kabut."
    kolonel_mayer "Artileri kita sudah tiba. Biarkan gunung itu tahu kita ada di sini."

    scene black with dissolve
    "Para pengungsi berkerumun di depan balai bambu. Paman naik ke atas bangku kayu, napasnya masih belum teratur. Sumarno berdiri di barisan depan, Adik menggenggam ujung bajunya."
    paman "Dengar semua! Belanda sudah masuk Purwokerto siang ini."
    "Bisik-bisik menyebar di antara kerumunan. Seorang ibu menutup mulutnya dengan jarik."
    warga_pengungsi "Pak, bagaimana rumah kami? Sawah kami?"
    paman "Kota sudah jadi abu, Bu. Mereka tidak menemukan apa-apa yang bisa dipakai. Tapi mereka sedang menggeledah rumah-rumah, satu per satu. Dan mereka membawa meriam."
    "Sebuah siulan panjang membelah udara."
    paman "TIARAP! SEMUA MASUK KOLONG BALAI!"
    "DUAR! Tanah di lereng bawah posko meledak. Atap anyaman bambu bergetar, debu berjatuhan. Jeritan pecah di mana-mana. Sumarno menerjang Adik dan menutup tubuh kecil itu dengan badannya."
    "Dua dentuman lagi menyusul, makin dekat, lalu semuanya hening. Hanya ada suara bayi menangis dan batuk-batuk di antara debu."
    adik "Kak... itu bukan lampion lagi ya?"
    sumarno "(Pelan) Bukan, Dik."
    "Ibu merangkak mendekat, memeluk keduanya sekaligus. Tangannya gemetar hebat, tapi ia tidak menangis."

    "Sore menjelang senja. Kabut tipis mulai turun dari puncak gunung."
    "Para pengungsi memperbaiki tenda yang roboh. Sumarno memanggul sebatang bambu patah, tapi pandangannya kosong ke arah kota."
    paman "Ikut Paman sebentar, No."
    "Mereka berjalan ke belakang dapur umum, tempat kabut lebih pekat dan suara orang jauh teredam."
    paman "Semalam Paman bicara dengan Pak Lurah dan seorang utusan TNI. Pasukan kita mundur ke utara, dan mereka sedang membangun pertahanan di perbukitan. Tapi mereka buta soal kota. Tidak ada yang tahu ke mana Belanda bergerak, di mana mereka menaruh pos, kapan patroli lewat."
    sumarno "Maksud Paman...?"
    paman "Mereka butuh mata di dalam kota. Orang yang hafal gang, lumbung, dan sumur. Orang yang bisa membawa makanan ke hutan tanpa ketahuan."
    sumarno "Paman yang dulu melarang Marno. Paman bilang siapa yang akan melindungi Ibu dan Adik kalau Marno kenapa-kenapa."
    paman "Dulu perang itu masih jauh, No. Sekarang perang itu sudah menembaki tenda adikmu. Menyuruhmu diam di sini sama saja menyuruhmu menunggu peluru."

    if chapter_2_route == "with_uncle":
        paman "Semalam kamu menahan diri demi ibumu. Itu bukan pengecut, No. Tapi sekarang yang paling melindungi keluargamu adalah memastikan Belanda tidak pernah sampai ke tenda ini."
    elif chapter_2_route == "with_laskar":
        paman "Jangan kira Paman tidak tahu ke mana kamu pergi semalam. Bau bensin itu tidak bisa bohong. Kamu sudah menyalakan api itu. Sekarang bantu Paman memastikan api itu tidak sia-sia."

    paman "Paman akan antar kamu lewat jalur tikus sampai tepi kota. Setelah itu kamu sendiri. Tapi bicaralah dulu pada ibumu."
    "Ibu sedang menyuapi Adik bubur sisa pagi tadi. Ibu mendongak dan langsung tahu dari raut wajahnya."
    ibu "Ibu sudah lihat dari caramu menatap kota itu sejak pagi."
    sumarno "Bu, Marno..."
    ibu "(Memotong lembut) Ibu tidak bisa menahan sungai yang mau mengalir, No. Tapi Ibu mau tanya satu hal. Kamu mau pergi karena marah, atau karena yakin?"
    sumarno "Dua-duanya, Bu. Tapi Marno tidak mau kita terus lari."
    "Ibu menatapnya, matanya berkaca-kaca, lalu mengangguk perlahan."
    sumarno "Semalam Marno janji sebelum matahari terbit, dan Marno nyaris telat. Kali ini Marno tidak berani janji soal waktu, Bu. Tapi Marno janji akan pulang."
    ibu "Janji yang bisa kamu tepati saja, No. Itu sudah cukup buat Ibu."
    "Ibu mencium kening Sumarno, lebih lama dari biasanya."
    adik "Kak, mau pergi lagi?"
    sumarno "(Berjongkok, tersenyum) Sebentar saja, Dik."
    "Adik menyodorkan satu-satunya cangkang keong yang ia punya."
    adik "Pegang ini. Biar kereta apinya ikut jaga Kakak. Tapi nanti dibalikin ya, soalnya gerbong batubaranya cuma satu ini."
    "Sumarno menerima cangkang itu dengan kedua tangan, lalu menyimpannya di saku dada."
    sumarno "Siap, Dik. Kakak balikin. Sama gerbong-gerbong barunya."

    "Matahari tenggelam di balik punggung gunung. Kabut turun semakin tebal, menelan jalan setapak di belakang posko."
    "Paman sudah menunggu di ujung jalan dengan sebuah buntelan kecil di punggungnya."
    paman "Ayo, No. Kabut ini kawan kita malam ini."
    "Sumarno menoleh sekali lagi. Ibu berdiri di depan tenda dengan Adik di sampingnya, dua sosok kecil yang makin buram diselimuti kabut."
    "Ibu mengangkat tangannya pelan. Sumarno membalas, lalu berbalik, dan keduanya menghilang ke dalam putihnya kabut menuju kota."
    jump tiba_di_kota_untuk_bertarung
