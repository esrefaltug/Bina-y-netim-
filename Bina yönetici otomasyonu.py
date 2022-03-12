import os
class Bina():
    
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True

    def program(self):
        secim=self.menuSecim()
        if secim==1:
            self.komsuEkle()
        if secim ==2:
            self.komsuCikar()
        if secim ==3:
            self.toplamAlınacakAidat()
        if secim ==4:
            self.masraf()
        if secim ==5:
            self.gelir()

    def menuSecim(self):
        secim=int(input("*****{} Otomasyonuna hoşgeldiniz****\n\n1-Komşu Ekle\n2-Komşu çıkart\n3-Toplam alınacak aidat \n4-Masraf gir \n5-gelir gir\n".format(self.ad)))
        while secim<1 or secim>5:
            secim=input("Lütfen 1-5 arası değer giriniz.")
        return secim

    def komsuEkle(self):
        id=1
        ad=input("Komşunun adını giriniz: ")
        soyad=input("Komşunun soyadını giriniz: ")
        kapıNo=input("Komşunun kapı numarasını giriniz: ")
        telNo=input("Komşunun telefon numarasını giriniz: ")

        with open("Komsular.txt","r") as dosya:
            komsuListesi=dosya.readlines()
        if len(komsuListesi)==0:
            id=1
        else:
            with open("Komsular.txt","r") as dosya:
                id=int(dosya.readlines()[-1].split(")")[0])+1

        with open("Komsular.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}\n".format(id,ad,soyad,kapıNo,telNo))

    def komsuCikar(self):
        with open ("Komsular.txt","r") as dosya:
            calisanlar=dosya.readlines()
        gCalisanlar=[]
        
        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[-1].split("-")))
        for calisan in calisanlar:
            print(calisan)

        secim=int(input("çıkarmak istediğiniz komşuyu seçiniz.".format(len(gCalisanlar))))
        calisanlar.pop(secim-1)
        
        sayac=1
        dCalisanlar=[]
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac)+")"+calisan.split(")")[1])
            sayac +=1

        
        with open("Komsular.txt","w") as dosya:
            dosya.writelines(dCalisanlar)
                               
            
            

    def toplamAlınacakAidat(self,hesap="a"):
        with open("Komsular.txt","w") as dosya:
            taidat=10*30
        print(taidat)
    def masraf(self):
        mmasraf=input("Bu ayki masraf ne kadar?")
        with open("Masraflar.txt","a+") as dosya:
            dosya.write(mmasraf)
        
    def gelir(self):
        ekgelir=int(input("Bu ayki ek gelir ne kadar?"))
        with open("Gelir.txt","a+") as dosya:
            ekgelir=dosya.writelines
        
    





bina=Bina("OZAN APTARTMANI")
while bina.calisma:
    bina.program()
        
        
