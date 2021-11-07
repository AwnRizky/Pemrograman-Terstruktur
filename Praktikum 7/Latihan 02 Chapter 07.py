namaFile = input("Masukan Nama File: ")
tambah = 'y'

try:
    file = open(namaFile, "r")
    while tambah == 'y' :
        data = input("Data Yang Mau Ditambahkan : ")
        file = open(namaFile, "a")
        file.write(data)
        tambah = input("Mau Lagi (y/n) : ")
        file = open(namaFile, "a")
        file.close()
except:
    print("File Tidak Ada")