n = int(input("Banyak baris bintang yang di inginkan : "))
def bintang(n):
    for i in range(n):
        print(('*'*(2*i+1)).center(2*n-1))

bintang(n)