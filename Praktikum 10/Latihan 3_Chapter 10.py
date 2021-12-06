dataFile = open('biodata.txt', 'r')

hasil = []

data = dataFile.readlines()

for i in range(len(data)):
    pecahData = data[i].split('|')
    dataDict = {'NIM': pecahData[0],
                'nama mahasiswa': pecahData[1],
                'alamat': pecahData[2].replace('\n', ' ')}
    hasil.append(dataDict)

print(hasil)

dataFile.close()