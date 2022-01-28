# sprawdż czy dany string jest palindromem (od tyłu jest taki sam jak od przodu) nie odwracając tekstu

def czy_palindrom(tekst):
    if len(tekst) < 1: # Jeśli doszliśmy aż tu, oznacza to, że to palindrom!
        return True
    else:
        if tekst[0] == tekst[-1]: # Czy pierwszy znak jest równy ostatniemy?
            return czy_palindrom(tekst[1:-1]) # jeśli tak funkcja wywoła samą siebie dla tego samego stringu z obciętym pierwszym i ostatnim znakiem
        else:
            return False # jeśli nie - to nie jest palindrom

print(czy_palindrom('kajak'))