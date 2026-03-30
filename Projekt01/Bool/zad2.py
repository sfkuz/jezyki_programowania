# link do zadania https://exercism.org/tracks/python/exercises/triangle



def trigon(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return 'odcinek misi być większy od 0'
    elif a == b and b == c:
        return 'trójkąt jest równoboczny'
    elif a == b or b == c:
        return 'trójkąt jest równoramienny'
    else:
        return 'trójkąt jest różnoramienny'

a = int(input('Podaj odcinek a: '))
b = int(input('Podaj odcinek b: '))
c = int(input('Podaj odcinek c: '))

wynik = trigon(a,b,c)
print(wynik)
