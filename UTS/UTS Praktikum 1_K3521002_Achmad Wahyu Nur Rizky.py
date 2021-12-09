tahun = int(input("Masukkan Tahun : "))
if tahun % 400 == 0:
    print("Tahun ", tahun, " Merupakan TAHUN KABISAT")
elif tahun % 400 != 0:
    if tahun % 100 == 0:
        print("Tahun ", tahun, " Bukan Merupakan TAHUN KABISAT")
    elif tahun % 100 != 0:
        if tahun % 4 == 0:
            print("Tahun ", tahun, " Merupakan TAHUN KABISAT")
        elif tahun % 4 != 0:
            print("Tahun ", tahun, " Bukan Merupakan TAHUN KABISAT")
