try:
    banyakAngka = int(input('Masukan Jumlah Bilangan Yang Diinginkan : '))
    data = []

    for i in range(banyakAngka):
        nomorData = i+1
        nilaiAngka = int(input("Masukan Angka Ke " + str(nomorData) + " = "))
        data += [nilaiAngka]
    data.sort(reverse=True)
    print(data)

except ValueError:
    print('Bukan Bilangan Bulat')