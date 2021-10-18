#variabel
bindo = int(input("Masukkan Nilai Bhs Indonesia : "))
ipa = int(input("Masukkan Nilai IPA : "))
mtk = int(input("Masukkan Nilai Matematika : "))
#if
if (bindo and ipa >= 60) and (mtk > 70):
    print("Status Kelulusan : LULUS")
else :
    print("Status Kelulusan : TIDAK LULUS")
