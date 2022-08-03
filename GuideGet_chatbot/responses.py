from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("Hai", "Hi", "Halo", "Apa Kabar", "Selamat Pagi", "Selamat Siang", "Selamat Malam", "Salam", "Ping", "P", "siang", "malam", "pagi", "helo", "hola"):
        return ("Halo, selamat datang di GuideGet, Kami akan membantu Kk dalam mencari Gadget impian Kk, silahkan ketik Minta Menu ya ka :)")

    if user_message in ("ada menu apa nih?" , "bisa minta menunya?", "tolong menunya", "bisa dibantu menunya", "mau ke menu lagi dong", "kembali ke menunya ka"):
        return ("Kk bisa tanya-tanya Aku tentang \nKetik 1 Mau Explore Gadget \nKetik 2 Mau Beli Gadget \nKetik 3 Mau Jual Gadget \nKetik 4 Mau Tukar Tambah Gadget")

    if user_message in ("1" , "Satu", "Mau Explore Gadget", "explore gadget dong", "explore please"):
        return ("Kk bisa tanya \nGadget terbaru apa? \nGadget termahal apa? \nGadget termurah apa?")
    
    if user_message in ("gadget terbaru apa ?", "Gadget terbaru apa ya?, Smartphone terbaru apa"):
        return ("Gadget terbaru ada Iphone 11 yang release 10 September 2019")

    if user_message in ("gadget termahal apa ?", "Gadget paling mahal apa ?, Smartphone paling mahal apa"):
        return ("Gadget paling mahal ada Apple iPhone 11 Pro Max with FaceTime - 512GB 4 GB Ram Space Gray harga IDR 24,310,900")

    if user_message in ("gadget termurah apa ?", "Gadget paling murah apa ?, Smartphone paling murah apa"):
        return ("Gadget paling murah ada Samsung Galaxy S10 Plus Dual Sim - 1Tb 8 GB Ram Ceramic White harga IDR 13,761,802")

    if user_message in ("2" , "Mau beli gadget", "Dua", "beli gadget dong", "beli please"):
        return ("Kk bisa tanya \nLokasi toko ada dimana saja ya ? \nApakah stock tersedia ? \nCara beli online gimana ya ?")

    if user_message in ("lokasi toko GuideGet dimana saja ya ?" , "dimana lokasi tokonya ?", "lokasi toko ada dimana saja ya", "toko GuideGet dimana saja ?"):
        return ("Kk bisa temukan lokasi Toko GuideGet di Jakarta, Tangerang, Depok, Bogor, silahkan mampir yang terdekat dengan Kk ya :)")

    if user_message in ("Apakah stock Iphone 11 ada ?" , "Apakah stock Iphone XS ada ?", "Apakah stock Iphone XR ada ?", "Apakah stock Samsung S10 Plus ada ?"):
        return ("Stock available di semua store GuideGet ka :)")

    if user_message in ("cara beli online gimana ya ?" , "apakah pembelian bisa via online ?", "bisa bantu pembelian online ?", "beli hpnya bisa online ?"):
        return ("Bisa ka, via link ini ya :)")

    if user_message in ("3" , "3.", "mau jual gadgetku dong", "jual gadget gimana ya", "tiga", "bisa dibantu untuk jual gadgetnya?"):
        return ("Kk bisa tanya \nLokasi toko ada dimana saja ya ? \nCara jual online gimana ya ?")

    if user_message in ("cara jual online gimana ya ?" , "apakah jual bisa via online ?", "bisa bantu penjualan via online ?", "jual hpnya bisa online ?"):
        return ("Bisa ka via link ini ya :)")

    if user_message in ("4" , "4.", "empat", "tukar tambah gadget", "tukar tambah please", "tukar tambah gadget dong"):
        return ("Tukar tambah kk bisa cek harga di aplikasi Kami ya, kemudian transaksi bisa langsung ke Toko GuideGet ya :)")

    if user_message in ("sip sip", "sip siip", "Terimakasih ya" , "Terimakasih", "Thankyou", "Dadah", "Selamat Tinggal", "Dah", "Daah", "Semoga harimu menyenangkan", "Ok makasih", "Sampai Jumpa Lagi", "Ok bye"): 
        return ("Terimakasih, tentang Gadget hubungi GuideGet ya :)", "Semoga harimu menyenangkan, tentang Gadget hubungi GuideGet ya :)")
    
    if user_message in ("nama kamu siapa?", "lu siapa?", "siapa sih lo?", "lu sape ?", "nama lo sape dah ?", "nama?"):
        return ("Namaku Gege, salam kenal Kak :)", "Halo, Aku Gege dari GuideGet", "Kenalin, Aku Gege dari GuideGet")

    if user_message in ("lu ngapain?", "pekerjaan kamu apa?", "lu kerja apa?", "tugas kamu apa?", "tugas lo ngapain?"):
        return ("Aku bantu Kk dalam mencari Gadget Impian Kk :)", "Tugasku jadi asisten Guidget supaya Kk bisa dapet Gadget impian Kk :)")

    if user_message in ("emang GuideGet apa si?", "apa tuh GuideGet?", "guideget itu apa ya?", "wah apa tuh GuideGet?", "guideget emang apa?"):
        return ("GuideGet adalah platform yang akan membantu dalam mencari Gadget yang Kk impikan :)")
        
    if user_message in ("emang gaidget apa ?", "apaan si gadget?", "emang godget apa sih?", "wah apa tuh gaid get?", "gatget emang apa?", "gat get itu apa sih"):
        return ("GuideGet ya Ka, pelan-pelan aja ngetiknya biar ga typo, Kami siap melayani kapanpun ko :)")
    
    if user_message in ("wow", "mantaaap!", "kereeen!", "mantap", "keren banget", "wiiih"):
        return ("Ada yang bisa Gege bantu lagi ka? :)")

    if user_message in ("kamu bisa apa?", "apa yang bisa anda lakukan?", "kamu bisa ngapain aja?", "lo bisa ngapain?", "apa kemampuan lo?"):
        return ("Kakak bisa tanya-tanya nama aku, apa yang aku lakukan dan yang berhubungan dengan GuideGet", "Pokoknya yang berhubungan sama Gadget bisa tanya Gege di GuideGet kak :)")

    if user_message in ("time", "jam?", "jamber", "jamberapa sekarang?" "jam berapa?"):
        return ("Sekarang jam " + str(datetime.now().strftime("%H:%M:%S")))

    if user_message in ("date", "tanggal?", "tanggal berapa?"):
        return ("Sekarang tanggal " + str(datetime.now().strftime("%d/%m/%Y")))

    if user_message in ("hari ini", "hari apa?", "hari berapa?"):
        return ("Hari ini hari " + str(datetime.now().strftime("%A")))
        
    return "Maaf kak, Gege ga ngerti :("