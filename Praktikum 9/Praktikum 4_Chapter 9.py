#import
import random

#function
def shuffleString(x, n):
    myList = []
    i = 0
    while i < n:
        kataAcak = [''.join(random.sample(x, len(x)))]
        if(kataAcak not in myList):
            myList += kataAcak
            i += 1
        print(myList)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)

