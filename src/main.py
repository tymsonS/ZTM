"""
Program zawiera przykładowe funkcje matematyczne
"""

# main.py
from flask import Flask, jsonify, request

app = Flask(__name__)

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

def pot13(n):
    """Zwraca 7 do potęgi n."""
    return 13 ** n


@app.get("/process")
def process():
    """Pierwszy endpoint"""
    result = {"2^10": pot2(10),
              "3^10": pot3(10),
              "5^3": pot5(3)}
    return jsonify(result)

@app.get("/test")
def test():
    """Pierwszy endpoint"""
    result1 = {"13^10": pot13(10)}
    return jsonify(result1)

# if __name__ == "__main__":
    # Jakis komentarz
    # app.run(host="0.0.0.0", port=8080, debug=False)
