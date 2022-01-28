# Napisz funkcję która powtórzy podany tekst zadaną ilość razy i zakończy go zadanym końcem linii. Domyślnym tekstem ma być 'SDA',
# a domyślnym końcem lii znak '!'

def powtorz_tekst(ilosc=2, tekst_do_powtorzenia='SDA', koniec_linii='!'):
    print(f'{tekst_do_powtorzenia * ilosc}{koniec_linii}') # Używamy f-string. Mnożymy tekst_do_wyświetlenia przez ilość i dodajemy koniec linii

powtorz_tekst(4, 'Hello', '\n') # Argumenty pozycyjne muszą zachować taką samą kolejność jak w deklaracji funkcji
powtorz_tekst(tekst_do_powtorzenia='Hello ', koniec_linii='?!\n', ilosc=4) # Podając argumenty nazwane nie musimy się przejmować kolejnością
powtorz_tekst(3, koniec_linii='Hehe\n', tekst_do_powtorzenia='Python ') # Łącząc argumenty pozycyjne i nazwane musimy zacząć od pozycyjnych zachowując ich kolejność, a potem nazwane nie musząc zachować kolejności
powtorz_tekst(3, 'Python ') # Argumenty pozycyjne. koniec_linii będzie miał wartość domyślną '!'
powtorz_tekst(tekst_do_powtorzenia='Python ') # Tylko jeden argument, reszta domyślna
