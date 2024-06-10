from Personel import Personel

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik
    def set_uzmanlik(self, yeni_deger):
        self.__uzmanlik = yeni_deger

    def get_deneyim_yili(self):
        return self.__deneyim_yili
    def set_deneyim_yili(self, yeni_deger):
        self.__deneyim_yili = yeni_deger

    def get_hastane(self):
        return self.__hastane
    def set_hastane(self, yeni_deger):
        self.__hastane = yeni_deger

    def __str__(self):
        return f"{super().__str__()}\nUzmanlık:{self.__uzmanlik}\nDeneyim Yılı:{self.__deneyim_yili}\nHastane Adı:{self.__hastane}"

    def maas_arttir(self, yuzde):
        return self.set_maas(self.get_maas()*(1 + yuzde/100))
