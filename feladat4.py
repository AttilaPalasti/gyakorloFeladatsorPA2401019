import math

def negy():
    n = 1
    k = 1
    if (k % 2 == 1) and (n > 0) and (math.pow(2, n) > k):
        # jó eset
        print("Proth-számok: ", end="")
        for db in range(1,10,1):
            proth = (k* math.pow(2, n)) + 1
            print(str(proth)+", ")
    proth = (k * math.pow(2,10)) + 1
    print(proth)
    else
        print("HIBA: Nem megfelelő számok!")

def negyb():
    n = 1
    k = 1
    print("Proth-számok: ", end="")
    while n>10: