def datastat(x):
 a = sum(x)/len(x)
 b = max(x)
 c = min(x)
 listData = [a, b, c]
 return listData

try:
 data = []
 banyakBilangan = int(input("Input Jumlah Bilangan Yang Diinginkan : "))
 for i in range(banyakBilangan):
  angka = int(input("Input Bilangan Bulat : "))
  data += [angka]
 print("Rata - Rata, Nilai Tertinggi, dan Nilai Terendah = ", str (datastat(data)))
except ValueError:
 print("Maaf Yang Anda Masukkan Bukan Angka")




