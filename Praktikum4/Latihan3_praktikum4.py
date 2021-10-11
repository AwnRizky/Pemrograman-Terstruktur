#total bensin
print("Total Liter Bensin Pak Budi")
jarakAC = int(input("Jarak(KM) = "))
jarakPerLiter = float(input("(KM/Liter) = "))
totalLiter = (jarakAC/jarakPerLiter)
print(totalLiter, "KM")

#total pengisian
kapasitasTangki = int(input("Kapasitas Tangki(L) = "))
totalIsi = float(totalLiter//kapasitasTangki)
print(totalIsi, "kali")