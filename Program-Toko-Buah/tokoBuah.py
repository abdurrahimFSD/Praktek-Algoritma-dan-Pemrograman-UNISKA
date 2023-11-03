print()
print('TOKO BUAH SEGAR MANIS')
print('*********************')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

print('Masukan Pilihan Buah: ')
print('===================> 1. Kiwi')
print('                     2. Mangga')
print('                     3. Alpukat')
print('                     4. Apel\n')

pilihanBuah = int(input('Masukkan pilihan Buah: '))
if pilihanBuah != 1 and pilihanBuah != 2 and pilihanBuah != 3 and pilihanBuah != 4:
    print('Pilihan yang dimasukkan salah')
    exit()
beratBuah = float(input('Masukkan berat buah: '))
hargaBuah = int(input('Masukkan Harga Buah: '))

potonganHarga = 0
potonganHargaTambahan = 0
hadiah = ''

if beratBuah <= 5:
    potonganHarga = 0

match pilihanBuah:
    case 1:
        if 5 < beratBuah <= 20:
            potonganHarga = 0.05
        elif beratBuah > 20:
            potonganHargaTambahan = 0.07
            potonganHarga = 0.05 + potonganHargaTambahan
    case 2:
        if 5 < beratBuah <= 20:
            potonganHarga = 0.025
        elif beratBuah > 20:
            potonganHargaTambahan = 0.07
            potonganHarga = 0.025 + potonganHargaTambahan
    case 3:
        if 5 < beratBuah <=10:
            potonganHarga = 0.07
        elif beratBuah > 10:
            potonganHarga = 0.07
            hadiah = 'Payung'
    case 4:
        if 5 < beratBuah <= 15:
            potonganHarga = 0.1
        elif beratBuah > 15:
            potonganHarga = 0.1
            hadiah = 'Tas'

hargaAsli = beratBuah * hargaBuah
hargaSetelahPotongan = hargaAsli - (hargaAsli * potonganHarga)

print()
print(f'Harga asli              : Rp {int(hargaAsli)}')
if potonganHarga != 0:
    print(f'Potongan harga          : {float(potonganHarga * 100)}%')
    print(f'Harga Setelah potongan  : Rp {int(hargaSetelahPotongan)}')

else:
    print('Anda tidak mendapat potongan harga')
if hadiah != '':
    print(f'Anda mendapatkan hadiah : {hadiah}')


