# Bob wypija 0.5 litra wody podczas godziny jazdy na rowerze. Zapytaj Boba ile jeździł na rowerze i powiedz mu ile PEŁNYCH litrów wody wypił

czas = float(input("Ile godzin jezdziles na rowerze Bob: ")) # Pobierz od użytkownika ilość godzin przejechanych na rowerz
litry = int(czas / 2) # Otrzymanie pełnych litrów poprzez rzutowanie na int
# litry = czas // 2 # Otrzymanie pełnych litrów poprzez użycie operatora //. W tym przypadku liczba zawsze będzie miała .0 na końcu, ponieważ to wciąż float
print(f'W trakcie {czas} godzin jazdy na rowerze wypiłeś {litry} pełnych litrów wody') # Wyświetl komunikat