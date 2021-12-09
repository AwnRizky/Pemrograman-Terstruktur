import datetime
from datetime import *
myFile = open('Data peminjaman buku.txt', "r")
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []

for line in myFile:
    change = line.split("|")
    data1 += change[0]
    data2 += change[1]
    data3 += change[2]
    data4 += change[3]
    data5 += change[4].strip()

again = str(input("Masukkan Kode Member : "))
if again in data1:
    find = True
    a = data1.index(again)
    dateNow = datetime.now()
    x = data5[a]
    x = datetime.strptime(x, '%y-%m-%d')
    rumus = x - dateNow
    dateReturn = datetime.date(dateNow)
    maxReturn = datetime.date(x)
else:
    print("Data TIdak Ada")
    myFile.close()
if find == True :
    rumus = datetime.date(dateNow) - maxReturn
    rumus = int(rumus.days)
    denda = 0
    if rumus >= 0:
        denda = 2000 *(rumus)
        rumus = abs(rumus)
    elif rumus <= 0:
        rumus = 0

    print("\nData Peminjaman Buku\n"
              "\nKode Member                    : ", data1[a],
              "\nNama Member                    : ", data2[a],
              "\nJudul Buku                     : ", data3[a],
              "\nTanggal Mulai Peminjaman       : ", data4[a],
              "\nTanggal Maks Peminjaman        : ", data5[a],
              "\nTanggal Pengembalian           : ", dateReturn,
              "\ntelat                          : ", rumus, "Hari"
                                                            "\nTotal denda                    :  Rp.", denda)

else:
    print("Data tidak ada")