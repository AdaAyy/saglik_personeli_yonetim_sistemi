from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd
import csv

def main():

    personel1 = Personel(1, "Filiz", "Ay", "Muhasebe", 20000)
    personel2 = Personel(2, "Pelin", "Derya", "Temizlik", 15000)


    doktor1 = Doktor(3, "Onur", "Özcan", "Dermatoloji", 10000, "Dermatolog", 15, "Ege Üniversitesi Araştırma Hastanesi")
    doktor2 = Doktor(4, "İlayda", "Solak", "Nöroloji", 9000, "Cerrah", 10, "Çiğli Eğitim ve Araştırma Hastanesi")
    doktor3 = Doktor(5, "Oğulcan", "Hilal", "Estetik", 11000, "Cerrah", 5, "İzmir Kent Hastanesi")


    hemsire1 = Hemsire(6, "Nehir", "Akbaş", "Yoğun Bakım", 30000, 35, "BLS Sertifikası", "Ege Yaşam Hastanesi")
    hemsire2 = Hemsire(7, "Duru", "Sucaklı", "Acil", 35000, 45, "CWCN Sertifikası", "Medical Park Hastanesi")
    hemsire3 = Hemsire(8, "Melih", "Dursun", "Beyin Cerrahi", 40000, 55, "CCRN Sertifikası", "Tınaztepe Hastanesi")


    hasta1 = Hasta(1, "Sena", "Mutlu", "05/03/1995", "Sakatlık", "Yatış")
    hasta2 = Hasta(2, "Zehra", "Öz", "24/02/2000", "Grip", "İlaç")
    hasta3 = Hasta(3, "Alp", "İnci", "26/05/2003", "Alerji", "İlaç")

    personeller = [personel1, personel2]
    hastalar = [ hasta1, hasta2, hasta3]
    doktorlar = [doktor1, doktor2, doktor3]
    hemsireler = [hemsire1, hemsire2,  hemsire3]

    all = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]
    for kisi in all:
        print(str(kisi) + "\n")

    bilgiler = []

    for personel in personeller:
        bilgi = {
            "personel_no": personel.get_personel_no(),
            "ad": personel.get_ad(),
            "soyad": personel.get_soyad(),
            "departman": personel.get_departman(),
            "maas": personel.get_maas()
        }
        bilgiler.append(bilgi)

    for doktor in doktorlar:
        bilgi = {
            "personel_no": doktor.get_personel_no(),
            "ad": doktor.get_ad(),
            "soyad": doktor.get_soyad(),
            "departman": doktor.get_departman(),
            "maas": doktor.get_maas(),
            "uzmanlik": doktor.get_uzmanlik(),
            "deneyim_yili": doktor.get_deneyim_yili(),
            "hastane": doktor.get_hastane()
        }
        bilgiler.append(bilgi)

    for hemsire in hemsireler:
        bilgi = {
            "personel_no": hemsire.get_personel_no(),
            "ad": hemsire.get_ad(),
            "soyad": hemsire.get_soyad(),
            "departman": hemsire.get_departman(),
            "maas": hemsire.get_maas(),
            "calisma_saati": hemsire.get_calisma_saati(),
            "sertifika": hemsire.get_sertifika(),
            "hastane": hemsire.get_hastane()
        }
        bilgiler.append(bilgi)

    for hasta in hastalar:
        bilgi = {
            "hasta_no": hasta.get_hasta_no(),
            "ad": hasta.get_ad(),
            "soyad": hasta.get_soyad(),
            "dogum_tarihi": hasta.get_dogum_tarihi(),
            "hastalik": hasta.get_hastalik(),
            "tedavi": hasta.get_tedavi()
        }
        bilgiler.append(bilgi)

