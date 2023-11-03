print()
print('INFORMASI TAGIHAN AIR')
print('=====================\n')
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

identitasPelanggan = int(input('ID Pelanggan: '))
namaPelanggan = str(input('Nama pelanggan: '))
alamatPelanggan = str(input('Alamat pelanggan: '))
golTarif = str(input('Gol Tarif [I-IV]: '))
bulanTahunTagihan = int(input('Bulan-Tahun Tagihan: '))
pemakaian = int(input('Pemakaian (kubik): '))
denda = int(input('Denda Rp: '))
print()

if golTarif == 'I':
    golonganPelanggan = 'Sosial'
    hargaAir = 1800
    biayaAdm = 8000
elif golTarif == 'II':
    golonganPelanggan = 'Rumah Tangga'
    hargaAir = 3100
    biayaAdm = 15000
elif golTarif == 'III':
    golonganPelanggan = 'Niaga'
    hargaAir = 4500
    biayaAdm = 25000
elif golTarif == 'IV':
    golonganPelanggan = 'Khusus'
    hargaAir = 6200
    biayaAdm = 100000

retribusiSampah = 5000
totalTagihan = biayaAdm + (hargaAir * pemakaian) + denda + retribusiSampah

print('Identitas Pelanggan :', identitasPelanggan)
print('Nama Pelanggan :', namaPelanggan)
print('Alamat Pelanggan :', alamatPelanggan)
print('Gol Tarif :', golTarif)
print('Bulan-Tahun Tagihan :', bulanTahunTagihan)
print('Gol Tarif [I-IV] :', golTarif)
print('Golongan Pelanggan :', golonganPelanggan)
print('Harga Air per kubik Rp. :', hargaAir)
print('Biaya Administrasi :', biayaAdm)
print('Retribusi Sampah :', retribusiSampah)
print('Pemakaian (kubik) :', pemakaian)
print('Denda:', denda)
print('Total Tagihan:', int(totalTagihan))


