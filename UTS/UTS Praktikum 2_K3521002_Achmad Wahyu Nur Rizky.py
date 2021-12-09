#Import
import random
import time

#Menu Level
print("========Bermain Bersama Matematika========")
time.sleep(1)
print("            MARI KITA BERMAIN            ")
print()
print("Menu Pilihan Level")
print("1. Level 1 (Penjumlahan)")
time.sleep(1)
print("2. Level 2 (Pengurangan)")
time.sleep(1)
print("3. Level 3 (Perkalian)")
time.sleep(1)
print("4. EXIT")

#Input Data
print()
level = int(input("Pilih Level Sesuai Kemampuan Anda : "))
lives = 3
score = 0

#Membuat Sistemnya
print()
print("Cara Bermain : ")
time.sleep(1)
print("-> Jawablah Sesuai Pertanyaan Yang Telah Disediakan")
print("-> Score Akan Bertambah Jika Jawaban Benar dan Sebaliknya")
print("-> Lives Akan Berkurang Jika Jawaban Salah")
print("-> Jika Ingin Keluar Dari Permainan Ketik KELUAR")
time.sleep(1)
print("PERMAINAN DIMULAI")
print()
time.sleep(1)
while True:
    if level == 1:
        if lives > 0:
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = a + b
            menjawab = input("Hasil Penjumlahan Dari  (" + str(a) + ") + (" + str(b) + ") : ")
            if menjawab == str("KELUAR"):
                time.sleep(1)
                print("ANDA TELAH KELUAR DARI PERMAINAN")
                exit(level)
            elif int(menjawab) == c:
                score += 2
                lives -= 0
                print("SELAMAT JAWABAN ANDA BENAR, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
            elif int(menjawab) != c:
                score -= 2
                lives -= 1
                print("SAYANG SEKALI JAWABAN ANDA SALAH, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
        elif lives == 0:
            print()
            time.sleep(1)
            print("NYAWA ANDA SUDAH HABIS")
            time.sleep(1)
            print("PERMAINAN TELAH BERAKHIR")
            break
    elif level == 2:
        if lives > 0:
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = a - b
            menjawab = input("Hasil Pengurangan Dari  (" + str(a) + ") - (" + str(b) + ") : ")
            if menjawab == str("KELUAR"):
                time.sleep(1)
                print("ANDA TELAH KELUAR DARI PERMAINAN")
                exit(level)
            elif int(menjawab) == c:
                score += 2
                lives -= 0
                print("SELAMAT JAWABAN ANDA BENAR, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
            elif int(menjawab) != c:
                score -= 2
                lives -= 1
                print("SAYANG SEKALI JAWABAN ANDA SALAH, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
        elif lives == 0:
            print()
            time.sleep(1)
            print("NYAWA ANDA SUDAH HABIS")
            time.sleep(1)
            print("PERMAINAN TELAH BERAKHIR")
            break
    elif level == 3:
        if lives > 0:
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            c = a * b
            menjawab = input("Hasil Perkalian Dari  (" + str(a) + ") * (" + str(b) + ") : ")
            if menjawab == str("KELUAR"):
                time.sleep(1)
                print("ANDA TELAH KELUAR DARI PERMAINAN")
                exit(level)
            elif int(menjawab) == c:
                score += 2
                lives -= 0
                print("SELAMAT JAWABAN ANDA BENAR, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
            elif int(menjawab) != c:
                score -= 2
                lives -= 1
                print("SAYANG SEKALI JAWABAN ANDA SALAH, SKOR ANDA MENJADI : " + str(score) + " (Lives : " + str(lives) + ")")
        elif lives == 0:
            print()
            time.sleep(1)
            print("NYAWA ANDA SUDAH HABIS")
            time.sleep(1)
            print("PERMAINAN TELAH BERAKHIR")
            break
    elif level == 4:
        print("ANDA KELUAR DARI PERMAINAN")
        break
    elif level != 1 or 2 or 3 or 4:
        print("MAAF PILIHAN ANDA SALAH, PERMAINAN DIBATALKAN")
        break
