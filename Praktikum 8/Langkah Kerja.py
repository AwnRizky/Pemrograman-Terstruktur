#list (a dan b)
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

a.insert(3, 10)
b.insert(2, 15)

a.append(4)
b.append(8)

a.sort()
b.sort(reverse=True)

#list (c dan d)
c = a[0:7]
d = b[2:9]

#list e
e = []
for i in range(len(c)):
    e.append(c[i]+d[i])

#list e to tuple
myTuple = tuple(e)
print(e)

#menghitung e
print(min(myTuple))
print(max(myTuple))
print(sum(myTuple))

#Buat String
myString = "Python adalah bahasa pemrograman yang menyenangkan"
mySet = set(myString)
print(mySet)

z = list(mySet)
z.sort()
print(z)