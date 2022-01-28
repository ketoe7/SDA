menu = ['krokiety', 'puree', 'schabowy', 'ryż', 'frytki'] # Stworzenie listy

print(menu[1]) # puree
menu.append('soja') # dodanie "soja" na koniec listy
print(menu) # wyświetl całą listę
menu.insert(-1, 'pizza') # Dodanie "pizza" w miejsce indeksu -1. Soja wciąż będzie ostatnia, a pizza przedostatnia
print(menu)

desery = ['sernik', 'szarlotka']
menu.extend(desery) # dołącz desery do menu
print(menu)
menu[1] = 'ziemniaki' # Zamiana puree na ziemniaki
print(menu)
menu.pop(5) # usunięcie elementu pod indeksem 5 (czyli "pizza")
print(menu)
print(menu.index('schabowy'))  # Zwrócenie indeksu odpowiadającego elementowi "schabowy"
menu.reverse() # Odwrócenie listy.
print(menu)
print(max(menu)) # Zwrócenie elementu maksymalnego czyli w przypadku stringów ostatniego alfabetycznie - ziemniaki
menu.sort() # Posortowanie listy (dla stringów alfabetycznie)
print(menu)























# menu = ['żurek', 'kotlet', 'pizza', 'pierogi', 'kapuśniak']
# print(menu[2])
# menu.append('jajecznica')
# print(menu)
# menu.insert(-2, 'pomidorowa')
# print(menu)
# desery = ['szarlotka', 'czekolada']
# menu.extend(desery)
# print(menu)
# menu[0] = 'łazanki'
# print(menu)
# del menu[6]
# print(menu)
# print(menu.index('pierogi'))
# print(menu.reverse())