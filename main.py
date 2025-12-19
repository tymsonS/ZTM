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
print('Dodaje by cos nie gralo')
print('Aby byl nowy commit')
print('Aby byl nowy commit 1')
print('Aby byl nowy commit 2')
print('Aby byl nowy commit 3')
print('Aby byl nowy commit 4')
print('Aby byl nowy commit 5')
print('Aby byl nowy commit 6')
print('Aby byl nowy commit 7')
print('Aby byl nowy commit 8')
print('Aby byl nowy commit 9')
print('Aby byl nowy commit 10')
print('Aby byl nowy commit 11')
print('Aby byl nowy commit 12')