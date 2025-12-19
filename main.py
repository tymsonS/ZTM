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
print('x-Ala ma kota, byle byl commit')
print('x-Dodaje by cos nie gralo')
print('x-Aby byl nowy commit')
print('x-Aby byl nowy commit 1')
print('x-Aby byl nowy commit 2')
print('x-Aby byl nowy commit 3')
print('x-Aby byl nowy commit 4')
x = 2
print(x+y)