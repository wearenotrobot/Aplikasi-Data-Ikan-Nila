"""
Aplikasi deteksi gempa terkini
Modularisasi dengan Function
Modularisasi dengan Package
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)
