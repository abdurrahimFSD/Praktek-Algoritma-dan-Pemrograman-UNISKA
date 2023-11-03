print()
print('Program Perhitungan ZAKAT')
print('=========================')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print('## Program Pembagian Harta Gonimah Perang ##')
print()

print('Pembagian Harta Gonimah Perang')
print('==============================')
namaPerang = input('Nama perang: ')
jumlahEmas = int(input('Jumlah (keping emas): '))
jumlahSahabat = int(input('Jumlah Sahabat r.hum (orang): '))

gramEmas = 4.25
hargaEmas = 667000
nilaiRampasan = jumlahEmas * gramEmas * hargaEmas
bagianNabi = nilaiRampasan * 1/5
bagianSahabat = (nilaiRampasan - bagianNabi) / jumlahSahabat

print('\n')

print('Hasil Pembagian')
print(f'Nilai rampasan Rp: {int(nilaiRampasan)}')
print(f'Bagian nabi Rp: {int(bagianNabi)}')
print(f'Bagian sahabat Rp: {int(bagianSahabat)}')