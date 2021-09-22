"""
init.py adalah package yang akan dibaca sebelum module di import
kode yang dijalankan adalah kode yang tidak di indentasi
"""
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    Tanggal: 24 Agustus 2021
    Waktu: 12:05:52 WIB
    Magnitudo: 4.0
    Kedalaman: 48 km
    Lokasi: LS: 1.48 BT: 134.01
    Pusat Gempa: Pusat Gempa berada di darat 18 km barat laut Ransiki
    Dirasakan: Dirasakan (Skala MMI): II-III Monokwari, II-III Ronsiki
    :return:
    """
    try:
        content = requests.get("https://www.bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li') #hasil findChildren berupa array
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        dirasakan = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.textK
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1] #blm bener
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan

        return hasil #prefer di pisah supaya terlihat proses akhirnya.
    else:
        return None

def tampilkan_data(result): #ini tidak dikirimkan ke mobile karena hanya dibaca di konsol.
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat LS:{result['koordinat']['ls']}, BT:{result['koordinat']['bt']}") #
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")



# if __name__ == '__main__':
#      print('Ini adalah package gempaterkini')

