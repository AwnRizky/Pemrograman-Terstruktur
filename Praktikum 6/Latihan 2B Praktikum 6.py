def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*', end='')
        print()

starFormation2(4)