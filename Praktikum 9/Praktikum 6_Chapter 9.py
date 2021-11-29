nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

for i in range(len(nilai)):
    nAkhir = (nilai[i]['mid'] + 2*(nilai[i]['uas']))//3
    nilai[i]['nAkhir'] = nAkhir
for i in  range(len(nilai)):
    if nilai[i]['nAkhir'] < 60:
        nilai[i]['status'] = 'TIDAK LULUS'
    else:
        nilai[i]['status'] = 'LULUS'
print("=" * 75)
print('NIM'.ljust(7), 'Nama'.ljust(20), 'MID'.ljust(7), 'UAS'.ljust(7), 'N.AKHIR'.ljust(14), 'STATUS'.ljust(14))
print("-" * 75)
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(7), end='')
    print(nilai[i]['nama'].ljust(20), end='')
    print(str(nilai[i]['mid']).rjust(7), end='')
    print(str(nilai[i]['uas']).rjust(7), end='')
    print(str(nilai[i]['nAkhir']).rjust(14), end='')
    print(str(nilai[i]['status'].rjust(14)))
print("=" * 75)