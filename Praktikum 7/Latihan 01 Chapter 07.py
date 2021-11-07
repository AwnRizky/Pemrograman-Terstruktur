masukanFile = input("Masukkan Nama File : ")
try:
    file = open(masukanFile, "r")
    print("Isi File", file, "adalah : ",
          file.read())
except:
    print("File Tidak Dapat Ditemukan")