print("----------------------------")
print("  PROGRAM HITUNG RATA-RATA  ")
print("----------------------------")

jumlah = 0
rata = 0
lagi = 'y'
while lagi=='y' :
    try:
        inputData = int(input("Masukkan Bilangan Bulat : "))
        jumlah += inputData
        rata += 1
        lagi = input("Lagi (y/n) : ")
    except ValueError:
        print("Bukan Bilangan Bulat")
print("Rata - ratanya adalah : ", jumlah/rata)
