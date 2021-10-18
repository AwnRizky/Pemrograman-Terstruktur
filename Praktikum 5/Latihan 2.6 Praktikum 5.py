from random import randint
hasil = randint(0, 100)
score = 100
print("Permainan tebak tebak angka")
while (True):
    tebak = int(input("Tebakan Anda : "))
    if(tebak>hasil):
        print("Tebakan Anda Terlalu Besar")
        print("Poin Anda Berkurang 2, sisa "+ str(score -2))
        score -= 2
    elif(tebak<hasil):
        print("Tebakan Anda Terlalu Kecil")
        print("Poin Anda Berkurang 2, sisa " + str(score - 2))
        score -= 2
    elif(score == 0):
        print("Poin sudah habis, anda tidak dapat melanjutkan permainan")
        break
    elif(int(tebak)==(hasil)):
        print("Tebakan Anda Benar :)")
        print("Anda Mendapatkan Poin Sebesar " + str(score))
        break
