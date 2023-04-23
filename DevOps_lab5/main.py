# Zaimportuj bibliotekę NumPy za pomocą menedżera pakietów pip
import numpy as np
import logging

# Ustaw poziom logowania
logging.basicConfig(level=logging.INFO)

# Loguj ważne informacje
logging.info("Start programu")

# Główny kod programu

# Funkcja odejmowania
def odejmowanie(a, b):
    return a - b

# Funkcja mnożenia
def mnozenie(a, b):
    return a * b

# Funkcja dzielenia
def dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "MIANOWNIK NIE MOŻE MIEĆ ZERA"


# Funkcja wykorzystująca bibliotekę NumPy
def funkcja_numpy(arr):
    return np.sum(arr)

# Przykładowe użycie funkcji
print(odejmowanie(5, 2))
print(mnozenie(5, 2))
print(dzielenie(6, 2)) # wypisze 3.0
print(dzielenie(6, 0)) # wypisze "MIANOWNIK NIE MOŻE MIEĆ ZERA"
print(funkcja_numpy([1, 2, 3]))

# Loguj informacje o zakończeniu działania programu
logging.info("Koniec programu")