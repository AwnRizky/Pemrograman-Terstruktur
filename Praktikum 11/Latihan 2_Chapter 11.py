from datetime import *

datenow = datetime.date(datetime.now())
datelater = datenow + timedelta(days=7)
myFile = open('Data peminjaman buku.txt', "a+")

while True:
    code = input("Input Kode Peminjam : ")
    name = input("Input Nama Peminjam : ")
    bookTitle = input("Input Judul Buku : ")

    data = code + "|" + name + "|" + bookTitle + "|" + str(datenow) + "|" + str(datelater) + "\n"
    myFile.write(data)

    print('')
    again = input("Lagi (Y/N) : ")
    if again == 'n' 'N' :
        print("Data Telah Di Input")
        break
    myFile.close()