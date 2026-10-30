class Calisan:
    zam_orani = 1.1
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
        return "Ad : {}  Soyad : {}  Maas: {}  Email: {}".format(self.isim, self.soyisim, self.maas, self.email)


calisan1 = Calisan("Ali", "Yılmaz", 5000)
calisan2 = Calisan("Ahmet", "Demir", 6000)


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bildigi_dil
    zam_orani = 1.2
    def bilgileri_goster(self):
        return "Ad : {}  Soyad : {}  Maas: {}  Email: {}  Dil: {}".format(self.isim, self.soyisim, self.maas, self.email, self.bildigi_dil)
    def dilini_soyle(self):
        return f"Bildiğim dil : {self.bildigi_dil}"

class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, calisanlar = None):
        super().__init__(isim, soyisim, maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self, calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())

yazilimci1 = Yazilimci("Ayşe", "Kara", 7000, "Python")
yazilimci2 = Yazilimci("Fatma", "Ay", 8000, "Java")

yonetici1 = Yonetici("Metin", "Ali", 10000)

yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yazilimci1)
yonetici1.calisanlari_goster()
print("*************")
yonetici1.calisan_sil(calisan1)
yonetici1.calisanlari_goster()
#yonetici2 = Yonetici("Pelin", "Katar", 11000, [yazilimci1, yazilimci2, calisan1])
#yonetici2.calisanlari_goster()

print(isinstance(yonetici1, Calisan))
print(issubclass(Calisan, Yazilimci))