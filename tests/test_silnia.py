"""
Testy funkcji silnia z modułu main.
"""

from main import silnia

def test_silnia_5():
    """Sprawdza, czy silnia(5) zwraca 120."""
    assert silnia(5) == 120