nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("=" * 60)
print('NIM'.ljust(14), 'Nama'.ljust(20), 'MID'.ljust(7), 'UAS'.ljust(7))
print("-" * 60)
for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(14), end='')
    print(nilai[i]['nama'].ljust(20), end='')
    print(str(nilai[i]['mid']).rjust(7), end='')
    print(str(nilai[i]['uas']).rjust(7))
print("=" * 60)