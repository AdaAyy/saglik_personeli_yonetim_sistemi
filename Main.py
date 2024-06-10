from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd
import csv


pd.set_option('future.no_silent_downcasting', True)  #Pandas ayarlarını değiştirme

def main():
    try:
        #Sınıf nesneleri oluşturma
        personel1 = Personel(1, "Filiz", "Ay", "Muhasebe", 6800)
        personel2 = Personel(2, "Pelin", "Derya", "Temizlik", 6000)


        doktor1 = Doktor(3, "Onur", "Özcan", "Dermatoloji", 10000, "Dermatolog", 15, "Ege Üniversitesi Araştırma Hastanesi")
        doktor2 = Doktor(4, "İlayda", "Solak", "Nöroloji", 9000, "Cerrah", 10, "Çiğli Eğitim ve Araştırma Hastanesi")
        doktor3 = Doktor(5, "Oğulcan", "Hilal", "Estetik", 11000, "Cerrah", 5, "İzmir Kent Hastanesi")


        hemsire1 = Hemsire(6, "Nehir", "Akbaş", "Yoğun Bakım", 6000, 35, "BLS Sertifikası", "Ege Yaşam Hastanesi")
        hemsire2 = Hemsire(7, "Duru", "Sucaklı", "Acil", 5000, 45, "CWCN Sertifikası", "Medical Park Hastanesi")
        hemsire3 = Hemsire(8, "Melih", "Dursun", "Beyin Cerrahi", 9000, 55, "CCRN Sertifikası", "Tınaztepe Hastanesi")


        hasta1 = Hasta(1, "Sena", "Mutlu", 1995, "Sakatlık", "Yatış")
        hasta2 = Hasta(2, "Zehra", "Öz", 2000, "Grip", "İlaç")
        hasta3 = Hasta(3, "Alp", "İnci", 1989, "Alerji", "İlaç")

        personeller = [personel1, personel2]
        hastalar = [ hasta1, hasta2, hasta3]
        doktorlar = [doktor1, doktor2, doktor3]
        hemsireler = [hemsire1, hemsire2,  hemsire3]

        all = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]
        for kisi in all:
            print(str(kisi) + "\n")

    except Exception as e:
        print("Hata:", e)

    try:
        bilgiler = []
        #Bilgileri sözlüklere yazma
        for personel in personeller:
            bilgi = {
                "Personel_No": personel.get_personel_no(),
                "Ad": personel.get_ad(),
                "Soyad": personel.get_soyad(),
                "Departman": personel.get_departman(),
                "Maas": personel.get_maas()
            }
            bilgiler.append(bilgi)

        for doktor in doktorlar:
            bilgi = {
                "Personel_No": doktor.get_personel_no(),
                "Ad": doktor.get_ad(),
                "Soyad": doktor.get_soyad(),
                "Departman": doktor.get_departman(),
                "Maas": doktor.get_maas(),
                "Uzmanlik": doktor.get_uzmanlik(),
                "Deneyim_Yili": doktor.get_deneyim_yili(),
                "Hastane": doktor.get_hastane()
            }
            bilgiler.append(bilgi)

        for hemsire in hemsireler:
            bilgi = {
                "Personel_No": hemsire.get_personel_no(),
                "Ad": hemsire.get_ad(),
                "Soyad": hemsire.get_soyad(),
                "Departman": hemsire.get_departman(),
                "Maas": hemsire.get_maas(),
                "Calisma_Saati": hemsire.get_calisma_saati(),
                "Sertifika": hemsire.get_sertifika(),
                "Hastane": hemsire.get_hastane()
            }
            bilgiler.append(bilgi)

        for hasta in hastalar:
            bilgi = {
                "Hasta_No": hasta.get_hasta_no(),
                "Ad": hasta.get_ad(),
                "Soyad": hasta.get_soyad(),
                "Dogum_Tarihi": hasta.get_dogum_tarihi(),
                "Hastalik": hasta.get_hastalik(),
                "Tedavi": hasta.get_tedavi()
            }
            bilgiler.append(bilgi)

        df = pd.DataFrame(bilgiler)                #DataFrame oluşturma
    except Exception as e:
        print("Hata", e)

    #Doktorları uzmanlık alanına göre gruplandırma
    doktor_grup = df.groupby("Uzmanlik", dropna=True).size()
    print(doktor_grup, "\n")

    print("5 yıldan fazla deneyime sahip doktor sayısı:", (df["Deneyim_Yili"] > 5).sum(), "\n")       #Deneyimi 5 yıldan fazla olan doktorların toplam sayısını yazdırma

    #Hasta adına göre alfabetik sıralama
    siralanmis_hasta = df[df['Tedavi'].isnull() == False].sort_values('Ad')
    kalan = df[df['Tedavi'].isnull()]
    df = pd.concat([kalan, siralanmis_hasta])
    df.index = range(1, len(df)+1)

    #Maaşa göre personelleri yazdırma
    personel_maas = df.loc[df["Maas"] > 7000, "Ad"].values
    print("Maaşı 7000 TL üzerinde olan personeller:", "," .join(personel_maas), "\n")

    #Doğum tarihine göre yazdırma
    hasta_dogum_tarihi = df.loc[df["Dogum_Tarihi"] > 1990, "Ad"].values
    print("1990'dan sonra doğan hastalar:", "," .join(hasta_dogum_tarihi), "\n")

    df.fillna(0, inplace=True)       #Boşluklara 0 değerini atama
    print(df)

    #Yeni DataFrame oluşturma
    new_df = df[['Ad', 'Soyad', 'Departman', 'Maas', 'Uzmanlik', 'Deneyim_Yili', 'Hastalik', 'Tedavi']]
    print("Yeni DataFrame:\n", new_df)

main()
