def faktorial (n) :
    if n == 0 :
        return 1
    else :
        return n*faktorial(n-1)

print('')
print('a. C(5, 3)')
print('Hasilnya : ')
a = faktorial(5)/(faktorial(5-3)*faktorial(3))
print(a)

print('')
print('b. P(10, 7)')
print('Hasilnya : ')
b =faktorial(10)/faktorial(10-7)
print(b)


