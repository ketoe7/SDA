# Napisz funkcję, która sprawdzi czy klient może wejść do parku rozrywki. Jeśli jego wzrost jest między 1.3m (włącznie),
# a 2m (wyłącznie) to może wejść do parku. W przeciwnym wypadku nie może

def sprawdz_czy_moze_wejsc(wzrost: float) -> bool: # deklaracja funkcji, dajemy znać, że chcemy aby parametr wzrost był liczbą dziesiętną, a funkcja zwracała wartość logiczną
    if  1.3 <= wzrost < 2: # Sprawdzamy czy wzrost jest większy bądź równy 1.3m i JEDNOCZEŚNIE mniejszy niż 2m
        return True # Jeśli tak, zwróć prawdę
    else:
        return False # Jeśli nie, zwróć fałsz

def powitaj_goscia_w_parku(imie): # ta funkcja nic nie zwraca
    print(f'{imie}, witaj w naszym parku!') # Tylko wyświetla na ekranie komunikat

ilosc_osob = 105 # Aktualna ilość osób w parku
imie = input('Podaj swoje imie: ') # Pobierz imię od użytkownika
wzrost = float(input('Podaj wzrost w metrach: ')) # Pobierz wzrost od użytkownika. Pamiętaj o zrzutowaniu na float. W przeciwnym razie zmienna wzrost będzie przechowywała string
if sprawdz_czy_moze_wejsc(wzrost): # wywołanie funkcji ze wzrostem od uzytkownika jako warunek ifa. Funkcja zwraca True lub False wiec moe zostac uzyta jako warunek
    powitaj_goscia_w_parku(imie) # blok instrukcji dla spelnionego warunku. Wywołaj funkcję powitaj_goscia_w_parku(imie) z imieniem użytkownika
    ilosc_osob += 1 # blok instrukcji dla spelnionego warunku. Zwiększ aktualną ilość osób w parku
    print(f'W parku jest {ilosc_osob} osob') # blok instrukcji dla spelnionego warunku. Wyświetl komunikat
else:
    print(f'Przykro nam {imie}, nie mozesz wejsc do parku...') # blok instrukcji dla niespelnionego warunku. Wyświetl komunikat
