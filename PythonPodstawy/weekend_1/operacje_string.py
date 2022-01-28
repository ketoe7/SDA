# 1. Utworz string zlozony z pierwszego, środkowego i ostatniego znaku stringu "James"
# wynik = "Jms"
name = 'James'
srodek = len(name) // 2
print(name[0] + name[srodek] + name[-1])

# 2. Utworz string zlozony z 3 środkowych znaków stringu "JamesJunPolit"
# wynik = "Jun"
name = 'JamesJunPolit'
srodek = len(name) // 2 # obliczenie indeksu indeksu dla znaku znajdującego się w środku stringu. W tym przypadku jest to znak 'u' mający indeks 6
print(name[srodek-1:srodek+2]) # korzystamy z cięcia stringów żeby wyciągnąć 3 środokwe znaki

# 3. Wstaw string 'Python' w środek stringu 'CoolCool'
tekst = 'CoolCool'
srodek = (len(tekst)-1) // 2 # Obliczenie indeksu znaku, po którym wstawimy 'Python' W tym przypadku to znak 'l' o indeksie 3
wynik = tekst[:srodek+1] + 'Python' + tekst[srodek+1:] # Znowu wykorzystujemy cięcie list. Najpierw bieżemy pierwszy kawałek do ostatniego znaku przed wstawieniem 'Python', czyli 'l'. Musimy użyć srodek+1 w tekst[:srodek+1] bo ostatni znak przy cięciu list nie jest brany pod uwagę. Następnie dodajemy 'Python' i na końcu wyświetlamy ostatnią część, czyli 'Cool'
print(wynik)

# 4. Znajdź ilość wystąpień podciągu "to" nie uwzględniając wielkości liter w stringu:
# "To piekny dzien, a python toto super jezyk, tato"
# wynik: "'to' wystapilo 4 razy"
tekst = 'To piekny dzien, a python toto super jezyk, tato'
szukaj = 'to'
print(f'to wystapilo {tekst.lower().count(szukaj)} razy') # lower() zmieni wszystkie znaki na małe, a count(szukaj) zwróci ilość wystąpień 'to' na stringu z już tylko małymi literami

# 5. Odwróc dowolny string
tekst = 'Zdanie do odwrocenia'
print(tekst[::-1]) # Od pierwszego znaku do ostatniego z krokiem -1, czyli odwracamy string

# 5. Znajdź pozycję pierwszego i ostatniego wystąpienia podciągu znaków "Bob" w zdaniu:
# "Bob jest python developerem. Bob pracuje w NASa"
# Użyj funkcji find() i rfind()
tekst = 'Bob jest python developerem. Bob pracuje w NASa'
szukaj = 'Bob'
pierwsze = tekst.find(szukaj) # funkcja find(szukaj) zwraca indeks pierwszego wystąpienia słowa pod zmienną 'szukaj' w tekście
ostatnie = tekst.rfind(szukaj) # funkcja rfind(szukaj) zwraca indeks ostatniego wystąpienia słowa pod zmienną 'szukaj' w tekście
print(f'Pozycja pierwszego wystapienia "Bob": {pierwsze}')
print(f'Pozycja ostatniego wystapienia "Bob": {ostatnie}')

# 6. W stringu 'Bob jest python developerem. Bob pracuje w NASa' zamien wszystkie spacje na -
tekst = 'Bob jest python developerem. Bob pracuje w NASa'
print(tekst.replace(' ', '-')) # Funkcja replace(znak_do_zmiany, znak_na_ktory_zamieniamy) zamienia wszystkie wystąpienia podanego znaku na inny znak

# 7. W stringu 'Bob jest python developerem. Bob pracuje w NASa' usun wszystkie spacje
tekst = 'Bob jest python developerem. Bob pracuje w NASa'
print(tekst.replace(' ', '')) # zamieniając znak na pusty string usuwamy ten znak

# 6. wydrukuj liczbę pi za pomocą f-string i zmiennych:
width = 10
precision = 4
value = 3.142654
wynik:  3.14
print(f'Liczba pi: {value:{width}.{precision}f}') # W tym przypadku width oznacza ile miejsc ma zajmować liczba, a precision ile ma być znaków po przecinku. Zwróć uwagę co się dzieje gdy width jest większe niż ilość cyfr - szerokość zostanie uzupełniona spacjami
