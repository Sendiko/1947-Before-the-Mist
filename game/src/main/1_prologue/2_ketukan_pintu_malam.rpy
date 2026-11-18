label night_knock:
    scene black with fade
    "Malam itu, suara jangkrik terdengar di antara kebun yang rimbun. Sumarno terbangun ketika waktu tahajud tiba."
    sumarno "Loh? Paman di mana? Perasaan tadi Paman tidur di ruang tamu."
    sumarno "Ah, mungkin sedang ronda. Nanti juga pulang sendiri. Salat dulu saja."

    "Setelah selesai salat, warna oranye tampak di antara gorden jendela. Paman datang tergesa-gesa dari pintu depan."
    paman "Eh, No, sudah bangun?"
    sumarno "Iya, Paman. Baru salat tahajud. Di luar ada apa? Kebakaran?"
    paman "No, dengarkan baik-baik. Jangan panik. Belanda sudah mulai mendekati Purwokerto."
    paman "Sekarang bangunkan Ibu dan Adik. Bantu mereka membawa barang berharga. Kita bersiap untuk evakuasi."
    sumarno "Hah, evakuasi? Ke mana, Paman? Terus nanti kota kita bagaimana? Ada pasukan laskar?"
    paman "Sudah tanya-tanya nanti saja! Kita harus pergi sekarang!"

    "Sumarno membangunkan Ibu dan Adik. Di luar, keadaan semakin ricuh dan teriakan terdengar di mana-mana."
    sumarno "Bu, bangun, yuk. Kita harus pergi sekarang."
    ibu "Hah? Pergi? Ada apa? Mau ke mana?"
    sumarno "Belanda, Bu. Kita harus pergi sekarang. Nanti kita dibantu Paman."
    ibu "Adik, ayo bangun. Taruh baju-bajumu di tas."
    adik "Kenapa, Bu?"
    ibu "Nanti Ibu jelaskan. Yuk, bangun dulu. Kita bersiap pergi."

    "Mereka meninggalkan rumah dan menyusuri jalan desa menuju lereng Gunung Slamet."
    paman "Barang-barang sudah semua, Dek? No?"
    ibu "Sudah."
    sumarno "Sudah, Paman."
    paman "Ikuti Paman. Di lereng Gunung Slamet sudah ada posko evakuasi."
    pasukan_laskar "No! Keluarga aman? Sudah tahu arahan evakuasi?"
    sumarno "Iya! Ke arah lereng Gunung Slamet, kan?"
    pasukan_laskar "Iya. Di sana sudah ada papan tanda jalan, ikuti saja. Sekarang kami sedang menyiapkan bumi hangus sebelum pasukan Belanda datang. Mau ikut?"
    paman "No! Sudah, tidak usah aneh-aneh kamu!"

    menu:
        "Memastikan Ibu dan Adik selamat sampai posko.":
            jump with_uncle
        "Bergabung dengan pasukan laskar untuk mempertahankan kota.":
            jump with_laskar