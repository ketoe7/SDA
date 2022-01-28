# Stwórz funkcję która na podstawie wagi i wzrostu obliczy bmi
# bmi = waga_w_kilogramach / (wzrost_w_metrach^2)

moja_waga = 88.0
moj_wzrost = 192.0

def calculate_bmi(waga=moja_waga, wzrost=moj_wzrost): # deklaracja funkcji def nazwa_funkcji(param1, param2, ...): Zastosowano parametry opcjonalne. W przypadku wywołania funkcji bez parametrów zostaną użyte wartości domyślne
    bmi = waga / ( (wzrost / 100)**2) # oblicz bmi na podstawie wzrostu przekształconego z cm na metry i wagi w kg
    if bmi < 18.5: # jesli bmi jest mniejsze niz 18.5 przejdz do bloku instrukcji wciętych pod tym warunkiem
        return f'twoje BMI równe: {bmi:4.1f} jest ponizej normy'
    elif bmi > 25: # jesli bmi > 25 wejdz w ten blok
        return f'twoje BMI równe: {bmi:4.1f} jest powyzej normy'
    elif bmi < 10: # jesli bmi < 10 wejdz w ten blok
        return f'twoje BMI równe: {bmi:4.1f} jest w krytycznie niskie!'
    else: # jeśli bmi nie spelnia ŻADNEGO poprzedniego warunku, wejdź tutaj
        return f'twoje BMI równe: {bmi:4.1f} jest w normie'


waga_uzytkownika = float(input('Wprowadź swoją wagę w kilogramach: ')) # pobierz od użytkownika jego wagę. input zwraca string, a my chcemy liczbę dziesiętną więc musimy zrutować wynik na float
wzrost_uzytkownika = float(input('Wprowadź swoj wzrost w cm: ')) # analogicznie dla wzrostu
print(calculate_bmi(waga_uzytkownika, wzrost_uzytkownika)) # wywołanie funkcji z parametrami
print(calculate_bmi()) # wywołanie funkcji bez podania parametrów
