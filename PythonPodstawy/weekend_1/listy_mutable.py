# Stwórz funkcję, która będzie dodawała do podany element do podanej listy tylko w przypadku gdy element jest parzysty.
# Gdy do funkcji nie przekażemy żadnej listy jako drugi argument funkcja powinna stworzyć pustą listę i do niej dodać
# element. Każde ponowne wywołanie funkcji bez podania drugiego parametru ma zwrócić nową listę

# pamiętaj: NIGDY nie używaj obiektów mutowalnych jako wartości domyślne parametrów funkcji
def append_if_even(elem, lst=None): # Ta linijka, deklaracja funkcji jest wykonywana tylko raz przy uruchomieniu skryptu. Za każdym razem gdy wywołamy tę funkcję bez parametru "lst" będzie wskazywało na None (który jest niemutowalny, nie da się go zmienić). Kolejne wywołania będą zawsze w lst mieć None
    if lst is None: # poprawna obsługa przypadku w którym "lst" jako obiekt mutowalny nie został przekazany do funkcji
        lst = []
    if elem % 2 == 0: # sprawdzamy czy element jest parzysty
        lst.append(elem) # jeśli tak, dodajemy do listy
    return lst # zwracamy zmodyfikowaną listę

lista3 = [1, 2, 5]

append_if_even(1, lista3) # wywołujemy funkcję z podaniem listy "lista3"
print(lista3) # 1 jest liczbą nieparzystą więc nie zostanie dodane do listy
append_if_even(2, lista3) # wywołujemy funkcję z podaniem listy "lista3"
print(lista3) # lista jest obiektem mutowalnym, dlatego append() z wewnątrz funkcji zmodyfikował tę listę w miejscu i teraz lista3 = [1, 2, 5, 2]
append_if_even(4, lista3) # ponownie wywołujemy funkcję z podaniem tej samej listy "lista3"
print(lista3) # podaliśmy do funkcji tę samą listę, która jest mutowalnym obiektem więc ma ona cały czas dopisane 2 z poprzedniego wywołania funkcji i 4 z tego wywołania


lista2 = append_if_even(2) # wywołujemy funkcję bez podania parametru. Funkcja tworzy NOWĄ listę, dodaje do niej 2 (bo jest parzyste) i ją zwraca
print(lista2) # Wyświetla jednoelementową listę z 2 w środku
lista2 = append_if_even(4) # ponowne wywołanie funkcji bez parametru
print(lista2) # To już inna lista. Nie ma w niej 2 tylko samo 4. Tak powinno to działać

# ZŁA IMPLEMENTACJA. Tak nie robimy!
def wrong_append_if_even(elem, lst=[]): # pusta lista będąca obiektem mutowalnym jest użyta jako wartość domyślna. Ta linijka, deklaracja funkcji jest czytana przez Pythona tylko raz przy uruchomieniu skryptu. Za każdym razem gdy wywołamy funkcję bez drugiego argumentu lst będzie wskazywało ne tę samą listę stworzoną na początku programu, która jest mutowalna i za każdym anstępnym razem ma dopisaną wartość z poprzedniego wywołania
    if elem % 2 == 0: # sprawdzamy czy element jest parzysty
        lst.append(elem) # jeśli tak, dodajemy do listy
    return lst # zwracamy zmodyfikowaną listę. Przy następnym wywołaniu funkcji lst będzie wciąż miało ten element!


lista2 = wrong_append_if_even(2) # wywołujemy funkcję bez podania parametru.
print(lista2) # Wyświetla jednoelementową listę z 2 w środku
lista2 = wrong_append_if_even(4) # ponowne wywołanie funkcji bez parametru
print(lista2) # Zobaczymy listę z dwoma elementami: 2 i 4!!!




