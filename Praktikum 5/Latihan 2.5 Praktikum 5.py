from random import randint
hasil = randint(0, 100)
print("Permainan tebak tebak angka")
while (True):
    tebak = int(input("Tebakan Anda : "))
    if(tebak>hasil):
        print("Tebakan Anda Terlalu Besar")
    elif(tebak<hasil):
        print("Tebakan Anda Terlalu Kecil")
    else:
        print("Tebakan Anda Benar :)")
        break
