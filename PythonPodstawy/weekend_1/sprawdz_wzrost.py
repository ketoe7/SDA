# Zapytaj użytkownika o wzrost. Jeślśli jest między 1.3m (włącznie), a 2m (wyłącznie) to może wejść do parku.
# W przeciwnym wypadku nie może

wzrost = float(input('Podaj wzrost w metrach: ')) # Pobierz wzrost od użytkownika. Pamiętaj o zrzutowaniu na float. W przeciwnym razie zmienna wzrost będzie przechowywała string
if wzrost < 1.3 or wzrost >= 2: # Sprawdź czy wzrost jest poniżej 1.3 LUB powyżej lub równy 2
    print(f'Przykro nam, nie mozesz wejsc do parku...') # blok instrukcji dla spelnionego warunku
else:
    print(f'Witaj w parku!') # blok instrukcji dla niespełnionego warunku

