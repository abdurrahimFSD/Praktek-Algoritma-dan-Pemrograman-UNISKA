print()
print('Program Perhitungan ZAKAT')
print('=========================')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print('## PROGRAM Menghitung Zakat  ##')
print()

print('Pilihan Jenis Zakat')
print('==================> 1. Zakat Uang')
print('                    2. Zakat Hasil Tani')
print('                    3. Zakat Fitrah')
print()

jenisZakat =int(input('Pilih No Jenis Zakat [1-3]: '))
keteranganZakat = ''
nisab = ''
kadar = 0
haul = ''
jumlahHarta = 0
jumlahOrang = 0
jumlahZakat = 0

if jenisZakat == 1:
    keteranganZakat = 'Zakat Uang'
    nisab = '85 gram emas'
    kadar = 0.025
    haul = '1 Tahun'
    jumlahHarta = int(input('Jumlah uang yang dimiliki: '))
    jumlahZakat = kadar * jumlahHarta
elif jenisZakat == 2:
    keteranganZakat = 'Zakat Hasil Tani'
    nisab = '653 kg beras'
    kadar = 0.05
    haul = 'Setiap Panen'
    jumlahHarta = int(input('Jumlah hasil tani yang dimiliki: '))
    jumlahZakat = kadar * jumlahHarta
elif jenisZakat == 3:
    keteranganZakat = 'Zakat Fitrah'
    nisab = 'Hidup saat lebaran'
    kadar = 0.035
    haul = '1 tahun'
    jumlahOrang = int(input('Jumlah orang yang akan diberikan zakat: '))
    jumlahZakat = kadar * jumlahOrang
else:
    print('Jenis zakat yang dimasukkan tidak valid')

if jumlahZakat != '':
    print(f'Keterangan Zakat   : {keteranganZakat}')
    print(f'Nisab              : {nisab}')
    print(f'Kadar              : {kadar}')
    print(f'Haul               : {haul}')
    if jenisZakat == 1 or jenisZakat == 2:
        print(f'Jumlah harta   : {int(jumlahHarta)}')
    elif jenisZakat == 3:
        print(f'Jumlah harta       : {int(jumlahOrang)}')
    print(f'Jumlah zakat       : {int(jumlahZakat)}')

