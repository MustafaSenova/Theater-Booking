kategori2_1 = [["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ]
kategori2_2 = [["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ]
kategori4_1 = [["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ]
kategori4_2 = [["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ["-", "-", "-", "-", "-"],
               ]
kategori1 = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ]
kategori3 = [["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
             ]

file = open("indirim.txt")
filelist = []
dosyasatir = len(file.readlines())
file.seek(0)
for z in range(dosyasatir):
    filelist.append(file.readline().rstrip("\n"))
filedict = {"M-10": 10, "1-200": 200, "2-150": 150, "3-100": 100, "4-60": 60, "1-05-10-10": 10, "2-05-10-05": 5,
            "3-05-10-05": 5, "4-05-10-03": 3}
maxbilet = filedict[filelist[0]]
fiyat1 = filedict[filelist[1]]
fiyat2 = filedict[filelist[2]]
fiyat3 = filedict[filelist[3]]
fiyat4 = filedict[filelist[4]]
indirim1 = filedict[filelist[5]]
indirim2 = filedict[filelist[6]]
indirim3 = filedict[filelist[7]]
indirim4 = filedict[filelist[8]]
toplamciro = 0


def salonyazdir():
    for i in range(10):
        if i == 9:
            print(i + 1, end=" ")
        else:
            print(i + 1, end="  ")
        for k in range(5):
            print(kategori2_1[i][k], end=" ")
        print(end=" ")
        for k in range(10):
            print(kategori1[i][k], end=" ")
        print(end=" ")
        for k in range(5):
            print(kategori2_2[i][k], end=" ")
        print()
    for i in range(10):
        print(i + 11, end=" ")
        for k in range(5):
            print(kategori4_1[i][k], end=" ")
        print(end=" ")
        for k in range(10):
            print(kategori3[i][k], end=" ")
        print(end=" ")
        for k in range(5):
            print(kategori4_2[i][k], end=" ")
        print()


def biletal(kategori, biletsayi, indirim):
    global toplamciro
    if (kategori == 1):
        koltuk = ""
        alinanbilet = biletsayi
        while (biletsayi != 0):
            for i in range(10):
                x = kategori1[i].count("X")
                for k in range(kategori1[i].count("X"), x + biletsayi):
                    if (kategori1[i].count("X") == 10):
                        pass
                    else:
                        kategori1[i][k] = "X"
                        biletsayi -= 1
                        koltuk += str(i + 1) + "-" + str(k + 6) + "  "
            if (biletsayi == 0):
                print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                nettutar = (alinanbilet * fiyat1) - (alinanbilet * fiyat1 * indirim / 100)
                print("Bilet adedi : ", alinanbilet)
                print("Toplam tutar :", alinanbilet * fiyat1)
                print("Yapılan indirim : %", indirim)
                print("Net tutar : ", nettutar, "TL")
                toplamciro += nettutar

    elif (kategori == 2):
        koltuk = ""
        alinanbilet = biletsayi
        while (biletsayi != 0):
            for i in range(10):
                y = kategori2_2[i].count("X")
                for k in range(4, -1, -1):
                    if (biletsayi == 0):
                        break
                    if (kategori2_1[i].count("X") == 5 or kategori2_1[i][k] == "X"):
                        pass
                    else:
                        kategori2_1[i][k] = "X"
                        biletsayi -= 1
                        koltuk += str(i + 1) + "-" + str(k + 1) + "  "
                if (biletsayi == 0):
                    print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                    nettutar = (alinanbilet * fiyat2) - (alinanbilet * fiyat2 * indirim / 100)
                    print("Bilet adedi : ", alinanbilet)
                    print("Toplam tutar :", alinanbilet * fiyat2)
                    print("Yapılan indirim : %", indirim)
                    print("Net tutar : ", nettutar, "TL")
                    toplamciro += nettutar
                    break
                if (biletsayi > 0):
                    for k in range(kategori2_2[i].count("X"), y + biletsayi):
                        if (kategori2_2[i].count("X") == 5):
                            pass
                        else:
                            kategori2_2[i][k] = "X"
                            biletsayi -= 1
                            koltuk += str(i + 1) + "-" + str(k + 16) + "  "
                if (biletsayi == 0):
                    print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                    nettutar = (alinanbilet * fiyat2) - (alinanbilet * fiyat2 * indirim / 100)
                    print("Bilet adedi : ", alinanbilet)
                    print("Toplam tutar :", alinanbilet * fiyat2)
                    print("Yapılan indirim : %", indirim)
                    print("Net tutar : ", nettutar, "TL")
                    toplamciro += nettutar
                    break

    elif (kategori == 3):
        koltuk = ""
        alinanbilet = biletsayi
        while (biletsayi != 0):
            for i in range(10):
                x = kategori3[i].count("X")
                for k in range(kategori3[i].count("X"), x + biletsayi):
                    if (kategori3[i].count("X") == 10):
                        pass
                    else:
                        kategori3[i][k] = "X"
                        biletsayi -= 1
                        koltuk += str(i + 10) + "-" + str(k + 6) + "  "
            if (biletsayi == 0):
                print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                nettutar = (alinanbilet * fiyat3) - (alinanbilet * fiyat3 * indirim / 100)
                print("Bilet adedi : ", alinanbilet)
                print("Toplam tutar :", alinanbilet * fiyat3)
                print("Yapılan indirim : %", indirim)
                print("Net tutar : ", nettutar, "TL")
                toplamciro += nettutar

    elif (kategori == 4):
        koltuk = ""
        alinanbilet = biletsayi
        while (biletsayi != 0):
            for i in range(10):
                y = kategori4_2[i].count("X")
                for k in range(4, -1, -1):
                    if (biletsayi == 0):
                        break
                    if (kategori4_1[i].count("X") == 5 or kategori4_1[i][k] == "X"):
                        pass
                    else:
                        kategori4_1[i][k] = "X"
                        biletsayi -= 1
                        koltuk += str(i + 10) + "-" + str(k + 1) + "  "
                if (biletsayi == 0):
                    print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                    nettutar = (alinanbilet * fiyat4) - (alinanbilet * fiyat4 * indirim / 100)
                    print("Bilet adedi : ", alinanbilet)
                    print("Toplam tutar :", alinanbilet * fiyat4)
                    print("Yapılan indirim : %", indirim)
                    print("Net tutar : ", nettutar, "TL")
                    toplamciro += nettutar
                    break
                if (biletsayi > 0):
                    for k in range(kategori4_2[i].count("X"), y + biletsayi):
                        if (kategori4_2[i].count("X") == 5):
                            pass
                        else:
                            kategori4_2[i][k] = "X"
                            biletsayi -= 1
                            koltuk += str(i + 10) + "-" + str(k + 16) + "  "
                if (biletsayi == 0):
                    print("Rezerve edilen koltuklar (Sıra - Koltuk) : " + koltuk)
                    nettutar = (alinanbilet * fiyat4) - (alinanbilet * fiyat4 * indirim / 100)
                    print("Bilet adedi : ", alinanbilet)
                    print("Toplam tutar :", alinanbilet * fiyat4)
                    print("Yapılan indirim : %", indirim)
                    print("Net tutar : ", nettutar, "TL")
                    toplamciro += nettutar
                    break


def anamenu():
    print("********************************************")
    print("***************** ANA MENU *****************")
    print("********************************************")
    print("1. Rezervasyon")
    print("2. Salonu Yazdır")
    print("3. Yeni etkinlik")
    print("4. Toplam Ciro")
    print("0. Çıkış")
    print("********************************************")
    secimislem()


def secimislem():
    secim = int(input("Seçiminiz ? "))
    while (secim > 4 or secim < 0):
        print("Menü seçimleri 0-4 arasında olmalıdır. Lütfen yeniden giriş yapın ! ")
        secim = int(input(" "))

    if (secim == 1):
        kategorisecim = int(input("Kategori (1-4) ? "))
        while (kategorisecim > 4 or kategorisecim < 1):
            print("1 ile 4 arasında bir kategori seçimi yapılmalıdır. Lütfen tekrar giriniz ! ")
            kategorisecim = int(input())
        biletadet = int(input("Bilet Adet (1-10) ? "))
        while (biletadet < 1 or biletadet > maxbilet):
            print("Yanlış giriş!! Bilet adedi 1-10 arasında bir sayı olmalıdır.")
            biletadet = int(input("Lütfen tekrar bilet adedi giriniz (1-10) : "))
        if (kategorisecim == 1):
            toplamx = 0
            toplameksi = 0
            for i in range(10):
                toplamx += kategori1[i].count("X")
                toplameksi += kategori1[i].count("-")
            if (toplamx + biletadet > 100):
                print("1.Kategoride istediğiniz adette bilet kalmamıştır. Kalan bilet sayısı : ", toplameksi)
                print("Rezervasyon iptal edilmiştir.Ana menüye yönlendiriliyorsunuz..")
                anamenu()
            else:
                if (biletadet >= 5):
                    biletal(kategorisecim, biletadet, indirim1)
                    anamenu()
                else:
                    biletal(kategorisecim, biletadet, 0)
                    anamenu()

        if (kategorisecim == 2):
            toplamx = 0
            toplameksi = 0
            for i in range(10):
                toplamx += kategori2_1[i].count("X") + kategori2_2[i].count("X")
                toplameksi += kategori2_1[i].count("-") + kategori2_2[i].count("-")
            if (toplamx + biletadet > 100):
                print("1.Kategoride istediğiniz adette bilet kalmamıştır. Kalan bilet sayısı : ", toplameksi)
                print("Rezervasyon iptal edilmiştir.Ana menüye yönlendiriliyorsunuz..")
                anamenu()
            else:
                if (biletadet >= 5):
                    biletal(kategorisecim, biletadet, indirim2)
                    anamenu()
                else:
                    biletal(kategorisecim, biletadet, 0)
                    anamenu()
        if (kategorisecim == 3):
            toplamx = 0
            toplameksi = 0
            for i in range(10):
                toplamx += kategori3[i].count("X")
                toplameksi += kategori3[i].count("-")
            if (toplamx + biletadet > 100):
                print("1.Kategoride istediginiz adette bilet kalmamıştır. Kalan bilet sayısı : ", toplameksi)
                print("Rezervasyon iptal edilmiştir.Ana menüye yönlendiriliyorsunuz..")
                anamenu()
            else:
                if (biletadet >= 5):
                    biletal(kategorisecim, biletadet, indirim3)
                    anamenu()
                else:
                    biletal(kategorisecim, biletadet, 0)
                    anamenu()
        if (kategorisecim == 4):
            toplamx = 0
            toplameksi = 0
            for i in range(10):
                toplamx += kategori4_1[i].count("X") + kategori4_2[i].count("X")
                toplameksi += kategori4_1[i].count("-") + kategori4_2[i].count("-")
            if (toplamx + biletadet > 100):
                print("1.Kategoride istediğiniz adette bilet kalmamıştır. Kalan bilet sayısı : ", toplameksi)
                print("Rezervasyon iptal edilmiştir.Ana menüye yönlendiriliyorsunuz..")
                anamenu()
            else:
                if (biletadet >= 5):
                    biletal(kategorisecim, biletadet, indirim4)
                    anamenu()
                else:
                    biletal(kategorisecim, biletadet, 0)
                    anamenu()
    elif (secim == 2):
        salonyazdir()
        anamenu()

    elif (secim == 3):
        for i in range(10):
            for k in range(10):
                kategori1[i][k] = "-"
                kategori3[i][k] = "-"
        for i in range(10):
            for k in range(5):
                kategori2_1[i][k] = "-"
                kategori2_2[i][k] = "-"
                kategori4_1[i][k] = "-"
                kategori4_2[i][k] = "-"
        global toplamciro
        toplamciro = 0
        print("Etkinlik Yenilendi ! ")
        anamenu()
    elif (secim == 4):
        print("Toplam Ciro : ", toplamciro, "TL")
        anamenu()
    elif (secim == 0):
        print("Program sonlandı..")
        file.close()
        exit()


anamenu()
