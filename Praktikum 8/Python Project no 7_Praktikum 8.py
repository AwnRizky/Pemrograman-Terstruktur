def harga():
    buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
    buahlist = list(buah.values())
    buahlist.sort(reverse=True)
    harting = buahlist[0]
    for buah, buahlist in buah.items():
        if buahlist == max:
            print(buah,harting)
harga()

