try :
    from datetime import *

    def diffDAte(x):
        tanggal = datetime.date(datetime.now())
        selisih = abs(x - tanggal)
        print("Selisih Hari Antara Tanggal ", tanggal, end='')
        print(" dan ", x, end='')
        print(" adalah ", selisih, " hari.")

    x = date(2003, 4, 8)
    diffDAte(x)
except ValueError:
    print("Data yang anda input salah")