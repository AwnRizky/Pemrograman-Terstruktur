kodekaryawan = input("Masukkan Kode Karyawan : ")
namakaryawan = input("Masukkan Nama Karyawan : ")
golkaryawan = input("Masukkan Golongan Karyawan : ")
if(golkaryawan == 'A' or 'a'):
    GajiPokok = 10000000
    Potongan = 2.5
elif(golkaryawan == 'B' or 'b'):
    GajiPokok = 8500000
    Potongan = 2.0
elif(golkaryawan == 'C' or 'c'):
    GajiPokok = 7000000
    Potongan = 1.5
elif(golkaryawan == 'D' or 'c'):
    GajiPokok = 5500000
    Potongan = 1.0
else:
    print('Golongan Tidak Valid')

gajikotor = Potongan/100 * GajiPokok
gajibersih = GajiPokok-gajikotor

print("==============================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------")
print("Nama Karyawan : " + namakaryawan + " (Kode : " + kodekaryawan +")")
print("Golongan      : " + golkaryawan)
print("------------------------------")
print("Gaji Pokok : RP. ", GajiPokok)
print("Potongan(" + str(Potongan) + "%) : Rp.", int(gajikotor))
print("------------------------------")
print("Gaji Bersih : RP. ", int(gajibersih))