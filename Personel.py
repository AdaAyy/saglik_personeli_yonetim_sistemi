class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    def get_personel_no(self):
        return self.__personel_no
    def set_personel_no(self, yeni_deger):
        self.__personel_no = yeni_deger
    
    def get_ad(self):
        return self.__ad
    def set_ad(self, yeni_deger):
        self.__ad = yeni_deger

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self, yeni_deger):
        self.__soyad = yeni_deger

    def get_departman(self):
        return self.__departman
    def set_departman(self, yeni_deger):
        self.__departman = yeni_deger

    def get_maas(self):
        return self.__maas
    def set_maas(self, yeni_deger):
        self.__maas = yeni_deger

    def __str__(self):
        return f"Ad:{self.__ad}\nSoyad:{self.__soyad}\nPersonel No:{self.__personel_no}\nDepartman:{self.__departman}\nMaaş:{self.__maas}"
