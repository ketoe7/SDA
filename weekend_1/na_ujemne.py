# pobierz liczbę od użytkownika. Jeśli jest to liczba ujemna nic z nią nie rób i wyświetl na ekran. Jeśli to liczba dodatnia
# wyświetl jej przeciwność

number = float(input("Podaj liczbę: ")) # pobierz liczbę od użytkownika. Pamiętaj o zrutowaniu wyniku funkcji input na float. Inaczej zmienna number będzie przechowywała string
if number <= 0: # Sprawdź czy podana liczba jest mniejsza bądź równa 0
    print(number) # Jeśli tak, wyświetl tę liczbę
else: # W przeciwnym wypadku
    number *= -1 # pomnóż tę liczbę przez -1 żeby uzyskać liczbę przeciwną. number *= -1 to to samo co number = number * -1
    print(number) # wyświetl liczbę przeciwną
