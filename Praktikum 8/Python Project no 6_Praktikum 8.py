banyak = int(input("Banyak Buah/Sayuran yang ingin dimasukkan : "))
sayur = []

def sortStringByChar():
    for i in range(banyak):
        jenis = str(input("Masukan Nama Buah/Sayur  : "))
        sayur.append(jenis)
    sayur.sort(key=len, reverse=True)
    print("Data Buah/Sayur :", sayur)

sortStringByChar()