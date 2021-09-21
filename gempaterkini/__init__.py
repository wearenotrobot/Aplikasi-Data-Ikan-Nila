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

        hasil = dict()
        hasil['tanggal'] = tanggal #'24 Agustus 2021'
        hasil['waktu'] = waktu #'12:05:52 WIB'
        hasil['magnitudo'] = 4.0
        hasil['lokasi'] = {'ls': 1.48, 'bt': 134.01}
        hasil['pusat gempa'] = 'Pusat Gempa berada di darat 18 km barat laut Ransiki'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Monokwari, II-III Ronsiki'

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
    print(f"Lokasi LS:{result['lokasi']['ls']}, BT:{result['lokasi']['bt']}") #
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")



# if __name__ == '__main__':
#      print('Ini adalah package gempaterkini')

