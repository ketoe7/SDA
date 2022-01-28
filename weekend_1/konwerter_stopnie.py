# Stwórz konwerter, który przeliczy stopnie celsjusza podane od użytkownika na stopnie fahrenheita
# Fahrenheit = Celsjusz * 1.8 + 32

celsjusz = float(input('Ile stopni celsjusza chcesz przeliczyc na fahrenheity? ')) # pobranie od użytkownika ilości stopni celsjusza do przekonwertowania.
farenheit = celsjusz * 1.8 + 32 # wyliczenie stopni farenheita na podstawie celsjuszy (wzór powyżej w komentarzu)
print(str(celsjusz) + ' celsjuszy jest równe ' + str(farenheit) + ' fahrenheit\'ów') # wyświetl komunikat poprzez konkatenację (połączenie) stringów. Zwróć uwagę jak wyświetlić znak cudzysłowa, który jednocześnie został użyty jako rozpoczęcie stringa. Trzeba użyć \ który neutralizuje specjalne znaczenie cudzysłowia w tym miejscu