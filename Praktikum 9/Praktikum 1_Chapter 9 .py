def ubahHurufTeks(teks, a, b):
    myList = list(teks)
    banyakA = myList.count(a)
    for i in range(banyakA):
        myList[myList.index(a)] = b
    print(''.join(myList))

ubahHurufTeks('MATEMATIKA', 'T', 'S')
