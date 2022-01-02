#8.SORU 
print("LUTFEN PROGRAMA KAYİT OLUNUZ")
kullanici_adi=input("Kullanıcı adinizi giriniz: ")
kullanici_sifre=input("Sifrenizi giriniz: ")
print("BASARIYLA KAYIT OLDUNUZ, GİRİS SAYFASİNA YONLENDİRİLİYORSUNUZ..")

giris_hakki=3 #3 kere yanlıs girilirse programdan cıkıs yapılacak
while True:

    if giris_hakki>0:

        giris_hakki-=1
        girilen_ad=input("KULLANICI ADI:")
        girilen_sifre=input("SİFRE")
        if kullanici_adi!=girilen_ad:
            print("Kullanıcı adinizi yanlis girdiniz.")
        elif kullanici_sifre!=girilen_sifre:
            print("Sifrenizi yanlis girdiniz.")
        elif kullanici_adi==girilen_ad and kullanici_sifre==kullanici_sifre:
            print("Basarıyla giris yaptiniz...")
            break
        
    else:
        print("3'den fazla deneme yaptiniz,programdan cikis yapiliyor...")
        break

