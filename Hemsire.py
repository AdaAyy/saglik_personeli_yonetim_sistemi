from Personel import Personel

#Personel sınıfından kalıtılan hemşire sınıfını oluşturma 
class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    #Accessor/Mutator metodları
    def get_calisma_saati(self):
        return self.__calisma_saati
    def set_calisma_saati(self, yeni_deger):
        self.__calisma_saati = yeni_deger

    def get_sertifika(self):
        return self.__sertifika
    def set_sertifika(self, yeni_deger):
        self.__sertifika = yeni_deger

    def get_hastane(self):
        return self.__hastane
    def set_hastane(self, yeni_deger):
        self.__hastane = yeni_deger


    def __str__(self):
        return f"{super().__str__()}\nÇalışma_Saati:{self.__calisma_saati}\nSertifika:{self.__sertifika}\nHastane_Adı:{self.__hastane}"

    #Maaş arttırma fonksiyonu
    def maas_arttir(self, yuzde):
        return self.set_maas(self.get_maas()*(1 + yuzde/100))
