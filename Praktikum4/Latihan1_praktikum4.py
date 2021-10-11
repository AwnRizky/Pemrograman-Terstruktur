#tarif sewa
print("__________Rental Mobil IKY__________")
tarifAwal = int(input("Sewa 12 jam pertama : Rp. "))
tarifLanjutan = int(input("Sewa per jam setelahnya : Rp. "))

#total waktu
print("Waktu Meminjam")
jamAwal = int(input("jam : "))
menitAwal = int(input("menit : "))
print("Waktu Dikembalikan")
jamAkhir = int(input("jam : "))
menitAkhir = int(input("menit : "))
lamaJam = (jamAkhir-jamAwal)
lamaMenit = (menitAkhir-menitAwal)
totalWaktu = print(lamaJam, "jam ", lamaMenit, "menit")

#total harga
print("__________Total Harga__________")
tambahanWaktu = (lamaJam-12)
print(tambahanWaktu, "jam")
totalHarga = print("Rp. ", (tambahanWaktu*tarifLanjutan)+tarifAwal)

