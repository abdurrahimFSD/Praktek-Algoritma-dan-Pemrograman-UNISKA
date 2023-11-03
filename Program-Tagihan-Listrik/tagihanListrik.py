print()
print('PROGRAM TAGIHAN LISTRIK')
print('*********************')
print()
print('## NPM    : 2210010460   ##')
print('## NAMA   : ABDURRAHIM   ##')
print('## KELAS  : TI 2D BJB    ##')
print()

noReg = int(input("\nNo. Reg: "))
namaPelanggan = input("Nama Pelanggan: ")
tipePelanggan = input("Tipe Pelanggan (R1/R2/R3): ")
if tipePelanggan != "R1" and tipePelanggan != "R2" and tipePelanggan != "R3":
    print('Tipe Pelanggan Salah')
    exit()
angkaMeterBulanLalu = int(input("Angka meter bulan lalu: "))
angkaMeterBulanIni = int(input("Angka meter bulan ini: "))

banyakListrikTerpakai = angkaMeterBulanIni - angkaMeterBulanLalu

if tipePelanggan == "R1":
    keteranganPelanggan = "Rumah Tangga"
    biayaAdministrasi = 15000
    biayaPerKwh = 1200
    if banyakListrikTerpakai >= 300:
        biayaPemakaianListrik = (biayaPerKwh * 300) + ((banyakListrikTerpakai - 300) * 1.5 * biayaPerKwh) + biayaAdministrasi
    elif banyakListrikTerpakai < 300:
        biayaPemakaianListrik = (biayaPerKwh * banyakListrikTerpakai) + biayaAdministrasi

elif tipePelanggan == "R2":
    keteranganPelanggan = "Rumah Toko"
    biayaAdministrasi = 25000
    biayaPerKwh = 2225
    if banyakListrikTerpakai >= 450:
        biayaPemakaianListrik = (biayaPerKwh * 450) + ((banyakListrikTerpakai - 450) * 2 * biayaPerKwh) + biayaAdministrasi
    elif banyakListrikTerpakai < 450:
        biayaPemakaianListrik = (biayaPerKwh * banyakListrikTerpakai) + biayaAdministrasi
        
elif tipePelanggan == "R3":
    keteranganPelanggan = "Industri"
    biayaAdministrasi = 35000
    biayaPerKwh = 4250
    if banyakListrikTerpakai >= 950:
        biayaPemakaianListrik = (biayaPerKwh * 950) + ((banyakListrikTerpakai - 950) * 2.5 * biayaPerKwh) + biayaAdministrasi
    elif banyakListrikTerpakai < 950:
        biayaPemakaianListrik = (biayaPerKwh * banyakListrikTerpakai) + biayaAdministrasi

pajak = 0.1 * biayaPemakaianListrik
besar_tagihan = biayaPemakaianListrik + pajak

print("\n===== Data Tagihan Listrik =====")
print("No. Reg                :", noReg)
print("Nama Pelanggan         :", namaPelanggan)
print("Tipe Pelanggan         :", tipePelanggan)
print("Banyak Listrik Terpakai:", banyakListrikTerpakai, "kWh")
print("Keterangan Pelanggan   :", keteranganPelanggan)
print("Biaya Administrasi     : Rp", biayaAdministrasi)
print("Biaya per kWh          : Rp", biayaPerKwh)
print("Biaya Pemakaian Listrik: Rp", int(biayaPemakaianListrik))
print("Pajak                  : Rp", int(pajak))
print("Besar Tagihan          : Rp", int(besar_tagihan))
