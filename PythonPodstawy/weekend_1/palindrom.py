# sprawdż czy dany string jest palindromem (od tyłu jest taki sam jak od przodu)
tekst = 'Kobyła ma mały bok'
tekst_czysty = tekst.lower().replace(' ', '') # zamieniamy tekst na małe litery i usuwamy wszystkie spacje
if tekst_czysty == tekst_czysty[::-1]: # sprawdzamy czy tak zmodyfikowany tekst (tylko małe litery bez spacji) jest taki sam jak jego rewers (tekst_czysty[::-1]) odwraca string
    print(f'"{tekst}" jest palindromem')
else:
    print(f'"{tekst}" nie jest palindromem')

