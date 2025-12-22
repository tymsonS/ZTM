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
y = 3
print('x-Ala ma kota, byle byl commit-l')
print('x-Dodaje by cos nie gralo-k')
print('x-Aby byl nowy commit-a')
print('x-Aby byl nowy commit 1a')
print('x-Aby byl nowy commit 2b')
print('x-Aby byl nowy commit 3c')
print('x-Aby byl nowy commit 4d')
print('Aby byl nowy commit 5e')
print('Aby byl nowy commit 6f')
print('Aby byl nowy commit 7')
print('Aby byl nowy commit 8')
print('Aby byl nowy commit 9')
print('Aby byl nowy commit 10')
print('Aby byl nowy commit 11')
print('Aby byl nowy commit 12')
x = 2
print(x+y)
