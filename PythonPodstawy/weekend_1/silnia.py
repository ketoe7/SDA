# Silnia to operacja matematyczna, która dla podanej liczby zwraca iloczyn wszystkich liczb od 1 do tej liczby. Czyli:
# 5! = 1*2*3*4*5 = 120
# n! = 1*2*3*4*...*n
# 0 jest przypadkiem specjalnym. 0! = 1
# Napisz funkcję, która dla podanej liczby zwróci jej silnię

def silnia(number):
    if number == 0:
        return 1
    else:
        wynik = 1 # Zmienna przchowująca tymczasowy wynik
        for n in range(1, number + 1): # Iteruj liczby od 1 do podanej jako argument liczby
            wynik *= n # Pomnóż dotychczasowy wynik przez kolejną liczbę. wynik *= n to inaczej wynik = wynik * n
        return wynik # zwrócć wynik

print(silnia(5))





























# def silnia(n):
#     if n == 0:
#         return 1
#     else:
#         return n * silnia(n-1)