def HelloWorld():
    print("Hello World")

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)

def sumNatural(n):
    return n * (n + 1) / 2

HelloWorld()
print(silnia(5))
print(sumNatural(5))
