def HelloWorld():
    print("Hello World")

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)

def sumNatural(n):
    return n * (n + 1) / 2

def sredniaArytm(n):
    sum = 0
    for i in range(n):
        sum += int(input())
    return sum/n


HelloWorld()
print(silnia(5))
print(sumNatural(5))
print(sredniaArytm(2))
print('Ala ma kota, byle byl commit')
