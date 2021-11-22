banyak = int(input("Banyak Bilangan Yang Diinginkan : "))
bil = []

def kuadrat (bil):
    hasil = []
    for i in range(banyak):
        bilbul = int(input("Masukan Bilangan Bulat : "))
        bil.append(bilbul)
        bil.sort()
    for y in range(banyak):
        bilkuadrat = bil[y]**2
        hasil.append(bilkuadrat)
        hasil.sort()
    print("Data Bilangan : ", bil)
    print("Hasil Kuadrat Dari Data Bilangan : ", hasil)

kuadrat(bil)





