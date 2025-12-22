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

def czy_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

HelloWorld()
print('5! = ', silnia(5))
print('Suma pierwszych 5 liczb ciagu liczb naturalnych dodatnich: ', sumNatural(5))
print('Podaj dwie liczby z ktorych chcesz obliczyc srednia:')
print('Srednia z podanych liczb: ', sredniaArytm(2))
print('Czy 7 jest pierwsza: ', czy_pierwsza(7))

