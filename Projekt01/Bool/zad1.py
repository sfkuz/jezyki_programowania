# link do zadania https://exercism.org/tracks/python/exercises/leap



def rok(num):
    if num % 4 == 0 or num % 400 == 0:
        return f"rok {num} jest przęstepny"
    else:
        return 'rok nie jest przęstepny'

rok_usr = int(input('Podaj rok: '))
wynik = rok(rok_usr)
print(wynik)