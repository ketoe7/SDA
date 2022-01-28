# zapytaj o haslo
# sprawdz czy jest dluzsze niz 8 znakow i krotsze niz 30
# czy zaczyna sie od A, B, C lub D
# funkcja ma przyjmowac cale haslo i zwracac bool
# pokaz jaki typ parametru oraz jaka wartosc zwracana przez funckcje sa oczekiwane
# odpowiedni komunikat

def sprawdz_dlugosc_hasla(haslo: str) -> bool:
    dlugosc_hasla = len(haslo) # pobierz długość hasła (czyli ilość znaków z których składa się string)
    if 30 < dlugosc_hasla < 8 or haslo[0] not in 'ABCD': # połączenie dwóch warunków: czy długość nie jest w podanym zakresie i czy pierwszy znak nie jest jednym z A, B, C, D
    # if (dlugosc_hasla < 8 or dlugosc_hasla > 30) or not haslo.startswith( ('A', 'B', 'C', 'D') ): # Druga metoda za pomocą funkcji startswith, która wymaga jako argumentu krotki
        return False # Złe hasło
    else:
        return True # Dobre hasło


def zapytaj_o_dane(wiadomosc: str, typ_zwracany=str): # Funkcja pomocnicza pytająca użytkownika o dane. Przyjmuje dwa parametry: wiadomosc, która ma zostać wyświetlona użytkownikowi oraz typ zmiennej jaki ma zostać zwrócony
    dane = typ_zwracany(input(wiadomosc)) # Rzutujemy wynik funkcji input na typ który jest zapisany w zmiennej typ_zwracany
    return dane


haslo = zapytaj_o_dane('Podaj haslo: ') # Wywołanie funkcji zapytaj_o_dane bez drugiego parametru. Będzie on miał wartość domyślny czyli str
if not sprawdz_dlugosc_hasla(haslo):
    print('Zle haslo! Haslo musi miec minimum 8 znakow i maksimum 30 znakow i zaczynac się od A, B, C lub D.')
else:
    print('Bravo, dobre haslo')
