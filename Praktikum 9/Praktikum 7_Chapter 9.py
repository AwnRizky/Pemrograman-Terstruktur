mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*80)
print('NIM'.ljust(12),'NAMA MAHASISWA'.ljust(27),'TANGGAL LAHIR'.ljust(22),'TEMPAT LAHIR')
print('-'*80)

for i in mhs:
       isplit = i.split(':')
       nim = isplit[0]
       nama = isplit[1]
       tglahir = isplit[2].split('-')
       tglahir = tglahir[2] + '/' + tglahir[1] + '/' + tglahir[0]
       tempat = isplit[3]
       print(nim.ljust(12), end='')
       print(nama.ljust(27), end='')
       print(tglahir.ljust(22), end='')
       print(tempat.ljust(5))
print('='*80)