import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

myFile = open(path + '/file text.txt', 'r')

ganjil = 0
genap = 0

for i in myFile:
       if int(i)%2==0:
              genap += 1
       else:
              ganjil +=1

print('Banyak Bilangan Ganjil =', ganjil)
print('Banyak Bilangan Genap =', genap)