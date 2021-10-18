#variabel
bindo = int(input("Masukkan Nilai Bhs Indonesia : "))
ipa = int(input("Masukkan Nilai IPA : "))
mtk = int(input("Masukkan Nilai Matematika : "))
#if
if (bindo and ipa and mtk >= 0) and (bindo and ipa and mtk <= 100):
    if (bindo and ipa >= 60) and (mtk > 70):
        print("Status Kelulusan : LULUS")
    else:
        print("Status Kelulusan : TIDAK LULUS")
else:
    print("Maaf Input Ada Yang Tidak Valid")
