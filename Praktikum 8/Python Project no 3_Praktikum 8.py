try:
    listnama = []
    jumlah = int(input("Jumlah Nama Mahasiswa Yang Ingin di Input : "))
    for i in range(jumlah):
        nama = (input("Nama Mahasiswa : "))
        listnama.append(nama)
    listnama.sort()
    for y in range(jumlah):
        print(listnama[y], "(",  (len(listnama[y])), "Karakter )")
except ValueError:
    print("Data Yang dimasukkan Salah")