import random

# ZADANIE 1
rows = 8
cols = 8
p = 1 #pionek
k = int(input('podaj liczbę hetmanów(maksymalnie 5): ')) #hetmany
k_liczba = 0 #liczba hetmanów
p_liczba = False #liczba pionka
p_position = [] #pozycje hetmanów
k_position = [] #pozycja pionka
if k > 5:
    print('maksymalna liczba hetmanów 5, podaj mniejszą liczbę.')

plansza = [['.' for j in range(cols)] for i in range(rows)]

while k_liczba < k:
    r = random.randint(0, 7)
    c = random.randint(0, 7)

    if plansza[r][c] == '.':
        plansza[r][c] = 'H'
        k_liczba += 1
        k_position.append((r, c))

while not p_liczba:
    rp = random.randint(0, 7)
    cp = random.randint(0, 7)

    if plansza[rp][cp] == '.':
        plansza[rp][cp] = 'P'
        p_liczba = True
        p_position.append((rp, cp))


for row in plansza:
    print(" ".join(row))

