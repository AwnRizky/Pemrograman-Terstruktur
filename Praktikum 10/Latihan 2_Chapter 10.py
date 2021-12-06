import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

myFile = open(path + '/biodata.txt', 'a')

while True:
    nim = input('Masukkan NIM : ')
    nama = input('Masukkan Nama : ')
    alamat = input('Masukkan Alamat : ')
    data = nim + '|' + nama + '|' + alamat + '\n'
    myFile.write(data)

    print('')
    lanjut = input('Ingin Memasukkan Data Lagi ? (y/n) : ')
    if lanjut in ("n", 'N'):
        break