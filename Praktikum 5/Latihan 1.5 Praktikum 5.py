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

statusmenikah = int(input("Masukkan Status (1: Menikah, 2: Belum): "))

if(statusmenikah == 1):
        status = "Menikah"
        TunjMenikah = 10 / 100 * GajiPokok
        JumAnak = int(input("Masukkan jumlah Anak  : "))
        TunjAnak = 5 / 100 * GajiPokok
        TunjAnak = TunjAnak * JumAnak

elif (statusmenikah == 2):
    Status = "Belum Menikah"
    TunjMenikah = 0
    TunjAnak = 0
    JumAnak = "-"

else:
    print("Status Menikah Tidak Valid")

gajikotor = GajiPokok + TunjMenikah + TunjAnak
potongan = Potongan / 100 * gajikotor
gajibersih = GajiPokok-potongan

print("==============================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------")
print("Nama Karyawan  : " + namakaryawan + " (Kode : " + kodekaryawan +")")
print("Golongan       : " + golkaryawan)
print("Status Menikah : " + Status)
print("Jumlah Anak    : " + JumAnak)
print("------------------------------")
print("Gaji Pokok : RP. ", GajiPokok)
print("Tunjangan Menikah: Rp.", int(TunjMenikah))
print("Tunjangan Anak   : Rp.", int(TunjAnak))
print("------------------------------")
print("Gaji Kotor       : Rp.", int(gajikotor))
print("Potongan (" + str(Potongan) + "%)  : Rp.", int(potongan))
print("------------------------------")
print("Gaji Bersih : RP. ", int(gajibersih))