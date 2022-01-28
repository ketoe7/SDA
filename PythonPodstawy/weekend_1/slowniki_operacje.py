oceny = {'Alicja': 5, 'Ola': 3.5, 'Tomek': 4, 'Jan': 4.5}
oceny['Ola'] = 5 # Nadpisz wartość dla klucza 'Ola'
print(oceny)
del oceny['Jan'] # Usuń wpis dla klucza 'Jan'
print(oceny)
print(oceny.get('Alicja', -1)) # Spróbuj pobrać wartość dla klucza 'Alicja'. Jeśli nie ma takiego klucza, zwróc 0
print(oceny.get('Emili', -1)) # To sam dla nieistniejcego klucza

druga_grupa = {'Krzysztof': 4.5, 'Patryk': 5, 'Magda': 5, 'Sonia': 4} # Stwórz nowy słwnik
oceny.update(druga_grupa) # Włącz elementy słownika druga_grupa do sownika oceny
print(oceny)
print(list(oceny.keys())) # wyświetl listę wszystkich kluczy
print(list(oceny.values())) # wyświetl listę wszystkich wartości
print(list(oceny.items())) # wyświetl listę krotek z kluczami i wartościami