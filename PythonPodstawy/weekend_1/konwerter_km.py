# Stwórz konwerter, który przeliczy kilometry podane od użytkownika na mile
# 1 kilometr = 0.621371 mil

przelicznik = 0.621371 # przelicznik zapisany do zmiennej
kilometry = float(input('Ile kilometrow chcesz przeliczyc na mile? ')) # pobranie od użytkownika ilości kilometrów do przekonwertowania. Pamiętaj o rzutowaniu wyniku funkcji input na float. Inaczej zmienna kilometry będzie przechowywała string
mile = kilometry * przelicznik # wylicz odpowiadającą ilość mil
print(str(kilometry) + ' kilometrow jest równe ' + str(mile) + ' mil') # wyświetl komunikat poprzez konkatenację (połączenie) stringów
# print(f'{0} kilometrow jest równe {1} mil'.format(kilometry, mile)) # wyświetl komunikat za pomocą funkcji format.
# print(f'{kilometry} kilometrow jest równe {mile} mil') # wyświetl komunikat za pomocą f-string. Czyż nie czytelniejsze?:)