# Korzystając z rekurencji oblicz silnię danej liczby

def silnia(number):
    if number == 0: # warunek końcowy. Jeśli number jest równe 0, zwróc 1
        return 1
    else:
        return number * silnia(number-1) # w innym przypadku pomnóż number przez wynik silni(number-1). W końcu przy którymś wywołaniu number-1 będzie równe 0 wtedu silnia zwróci 1 i będziemy wracać z mnożeniem aż do początku

print(silnia(5))