print()
print('Data Gaji Pegawai')
print('=================')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

nip = int(input('Masukan NIP pegawai: '))
nama = str(input('Masukkan Nama pegawai: '))
golongan = int(input('Masukkan Golongan [1-3]: '))
if golongan != 1 and golongan != 2 and golongan != 3:
    print('Golongan Salah')
    exit()
jamKerja = int(input('Masukkan Jam Kerja per hari: '))
hariKerja = int(input('Masukkan Hari Kerja per bulan: '))
print()

if golongan == 1:
    statusPegawai = 'Tetap'
    gajiPokok = 7500000
    tunjangan = 0.15 * gajiPokok
   
elif golongan == 2:
    statusPegawai = 'Kontrak'
    gajiPokok = 5000000
    tunjangan = 0.1 * gajiPokok

elif golongan == 3:
    statusPegawai = 'Lepas'
    gajiPokok = 3500000
    tunjangan = 0.05
   
if jamKerja >= 9:
    uangMakan = (2 * 12500) * hariKerja
else:
    uangMakan = 12500 * hariKerja
uangTransportasi = 7500 * hariKerja
if jamKerja > 8:
    uangLembur = (jamKerja - 8) * hariKerja * 20000
else:
    uangLembur = 0
if hariKerja >= 26:
    bonus = 0.05 * gajiPokok
else:
    bonus = 0

gajiKotor = gajiPokok + tunjangan + uangMakan + uangTransportasi + uangLembur + bonus
pajakPPH = 0.1 * gajiKotor
gajiBersih = gajiKotor - pajakPPH

print('Status pegawai          : ', statusPegawai)
print('Gaji Pokok (Rp)         : ', gajiPokok)
print('Tunjangan               : ', int(tunjangan))
print('Uang Makan              : ', uangMakan)
print('Uang Transportasi (Rp)  : ', uangTransportasi)
print('Uang Lembur (Rp)        : ', uangLembur)
print('Bonus (Rp)              : ', int(bonus))
print('Gaji Kotor (Rp)         : ', int(gajiKotor))
print('Pajak PPH (Rp)          : ', int(pajakPPH))
print('Gaji Bersih (Rp)        : ', int(gajiBersih))