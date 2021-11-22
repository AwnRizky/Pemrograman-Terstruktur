listsayur = ["Bayam", "Kangkung", "Wortel", "Selada"]
while True :
    menu = print("Menu : \nA. Tambah Data Sayur \nB. Hapus Data Sayur \nC. Tampilkan Data Sayur")
    pilihan = str(input("Pilihan Anda : "))
    if pilihan == "A" or pilihan == "a":
        a = str(input("Jenis Sayur Yang Akan Ditambah : "))
        listsayur.append(a)
    elif pilihan == "B" or pilihan == "b":
        b = str(input("Jenis Sayur Yang Ingin Dihapus : "))
        listsayur.remove(b)
    elif pilihan == "C" or pilihan == "c":
        sayur = tuple(listsayur)
        print(sayur)
        continue
    print("Lanjut Memilih (Y/N)?", end='')
    lanjut = input()
    if lanjut == "Y" or lanjut == "y":
        print(menu)
    if lanjut == "n" or lanjut == "N":
        break
