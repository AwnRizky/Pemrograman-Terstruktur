#variabel
bindo = int(input("Masukkan Nilai Bhs Indonesia : "))
ipa = int(input("Masukkan Nilai IPA : "))
mtk = int(input("Masukkan Nilai Matematika : "))
#if
if (bindo and ipa and mtk >= 0) and (bindo and ipa and mtk <= 100):
    if (bindo and ipa >= 60) and (mtk > 70):
        print("Status Kelulusan : LULUS")
    else:
        sebab = ""
        if (bindo < 60):
            sebab += ("Nilai Bahasa Indonesia Kurang Dari 60 ")
        if (ipa < 60):
            sebab += ("Nilai IPA Kurang Dari 60 ")
        if (mtk < 60):
            sebab += ("Nilai MTK Kurang Dari 70 ")
        print("Status Kelulusan : TIDAK LULUS")
        print("Sebab : ")
        print(sebab)
else:
    print("Maaf Input Ada Yang Tidak Valid")
