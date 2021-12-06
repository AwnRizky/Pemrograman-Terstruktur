file = open('angka1.txt', 'r')
result_file = open('angka2.txt', 'w')

data = file.readline()
new_data = ''

for i in data:
    pisah = i.split('|')
    jumlah = int(pisah[0]) + int(pisah[1].replace('\n', ''))
    new_data += str(jumlah) + '\n'

result_file.write(new_data)
result_file.close()