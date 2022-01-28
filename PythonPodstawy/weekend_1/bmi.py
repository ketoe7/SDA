# Pobierz od użytkownika jego wagę i wzrost, a następnie oblicz jego bmi
# bmi = waga_w_kilogramach / (wzrost_w_metrach^2)

waga_uzytkownika = float(input('Wprowadź swoją wagę w kilogramach: ')) # pobierz od użytkownika jego wagę. input zwraca string, a my chcemy liczbę dziesiętną więc musimy zrutować wynik na float
wzrost_uzytkownika = float(input('Wprowadź swoj wzrost w cm: ')) # analogicznie dla wzrostu
bmi = waga_uzytkownika / ( (wzrost_uzytkownika / 100)**2) # oblicz bmi

if bmi < 18.5: # jesli bmi jest mniejsze niz 18.5 przejdz do bloku instrukcji wciętych pod tym warunkiem
    print(f'twoje BMI równe: {bmi:4.1f} jest ponizej normy')
elif bmi > 25: # jesli bmi > 25 wejdz w ten blok
    print(f'twoje BMI równe: {bmi:4.1f} jest powyzej normy')
elif bmi < 10: # jesli bmi < 10 wejdz w ten blok
    print(f'twoje BMI równe: {bmi:4.1f} jest krytycznie niskie!')
else: # jeśli bmi nie spelnia ŻADNEGO poprzedniego warunku, wejdź tutaj
    print(f'twoje BMI równe: {bmi:4.1f} jest w normie')