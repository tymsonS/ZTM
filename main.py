def HelloWorld():
    print("Hello World")

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)

HelloWorld()
print(silnia(5))
