#Hasta sınıfını oluşturma
class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    #Accessor/Mutator metodları
    def get_hasta_no(self):
        return self.__hasta_no
    def set_hasta_no(self, yeni_deger):
        self.__hasta_no = yeni_deger

    def get_ad(self):
        return self.__ad
    def set_ad(self, yeni_deger):
        self.__ad = yeni_deger

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self, yeni_deger):
        self.__soyad = yeni_deger

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    def set_dogum_tarihi(self, yeni_deger):
        self.__dogum_tarihi = yeni_deger

    def get_hastalik(self):
        return self.__hastalik
    def set_hastalik(self, yeni_deger):
        self.__hastalik = yeni_deger

    def get_tedavi(self):
        return self.__tedavi
    def set_tedavi(self, yeni_deger):
        self.__tedavi = yeni_deger

    def __str__(self):
        return f"Ad:{self.__ad}\nSoyad:{self.__soyad}\nHasta_No:{int(self.__hasta_no)}\nDoğum_Tarihi:{int(self.__dogum_tarihi)}\nHastalık:{self.__hastalik}\nTedavi:{self.__tedavi}"

    #Tedavi süresini hesaplayan fonksiyon
    def tedavi_suresi_hesapla(self):
        if self.__hastalik == "Alerji":
            sure1 = 3
        elif self.__hastalik == "Grip":
            sure1 = 5
        elif self.__hastalik == "Sakatlık":
            sure1 = 10

        if self.__tedavi == "İlaç":
            sure2 = 5
        elif self.__tedavi == "Yatış":
            sure2 = 3

        return sure1 + sure2
