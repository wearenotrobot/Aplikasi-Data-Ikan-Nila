"""
init.py adalah package yang akan dibaca sebelum module di import
kode yang dijalankan adalah kode yang tidak di indentasi
"""

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
    hasil = dict()
    hasil['tanggal'] = '24 Agustus 2021'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls': 1.48, 'bt': 134.01}
    hasil['pusat gempa'] = 'Pusat Gempa berada di darat 18 km barat laut Ransiki'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Monokwari, II-III Ronsiki'

    return hasil #prefer di pisah supaya terlihat proses akhirnya.


def tampilkan_data(result): #ii tidak dikirimkan ke mobile karena hanya dibaca di konsol.
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi LS:{result['lokasi']['ls']}, BT:{result['lokasi']['bt']}") #
    print(f"Pusat Gempa {result['pusat gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


# if __name__ == '__main__':
#      print('Ini adalah package gempaterkini')

