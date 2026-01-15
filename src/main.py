"""
Program zawiera przykładowe funkcje matematyczne
"""
def hello_world():
    """Wyświetla napis 'Hello World'."""
    print("Hello World")

def silnia(n):
    """Zwraca silnię liczby n (n!)."""
    if n == 1:
        return 1
    return n * silnia(n - 1)

def sum_natural(n):
    """Zwraca sumę pierwszych n liczb naturalnych dodatnich."""
    return n * (n + 1) / 2

def srednia_arytmetyczna(n):
    """Sprawdza, czy liczba n jest liczbą pierwszą."""
    suma = 0
    for _ in range(n):
        suma += int(input())
    return suma/n

def czy_pierwsza(n):
    """Zwraca największy wspólny dzielnik liczb a i b."""
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

def nwd(a, b):
    """Zwraca największy wspólny dzielnik liczb a i b."""
    while b > 0:
        pom = a
        a = b
        b = pom % b
    return a

def pot2(n):
    """Zwraca 2 do potęgi n."""
    return 2 ** n

def pot3(n):
    """Zwraca 3 do potęgi n."""
    return 3 ** n

def pot5(n):
    """Zwraca 5 do potęgi n."""
    return 5 ** n

def pot7(n):
    """Zwraca 7 do potęgi n."""
    return 7 ** n

if __name__ == "__main__":
    hello_world()
    print('5! = ', silnia(5))
    print('Suma pierwszych 5 liczb ciagu liczb naturalnych dodatnich: ', sum_natural(5))
    print('Podaj dwie liczby z ktorych chcesz obliczyc srednia:')
    print('Srednia z podanych liczb: ', srednia_arytmetyczna(2))
    print('Czy 7 jest pierwsza: ', czy_pierwsza(7))
    print('Nwd(17, 16) = ', nwd(17, 16))
    print('Nwd(8, 16) = ', nwd(8, 16))
    print('2^10 = ', pot2(10))
    print('3^10 = ', pot3(10))
    print('5^3 = ', pot5(3))
    print('7^3 = ', pot7(3))