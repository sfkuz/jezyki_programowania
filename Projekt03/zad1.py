import random

# ZADANIE 1
rows = 8
cols = 8
p = 1 #pionek
k = 0 #hetmany
while True:
    k = int(input('podaj liczbę hetmanów (maksymalnie 5): '))
    if 0 < k <= 5:
        break
    print('Maksymalna liczba hetmanów to 5, spróbuj ponownie.')
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


# ZADANIE 2
kto_bije = []
pr, pc = p_position[0] # pozycja pionka w linijce i kolumnie

for h in k_position:
    hr = h[0] # pozycja hetmana w linijce
    hc = h[1] # pozycja hetmana w kolumnie
    if (hr == pr) or (hc == pc) or (abs(hr - pr) == abs(hc - pc)): # abs żeby liczba nie była ujemna
        kto_bije.append(h)

if len(kto_bije) > 0:
    print(f'hetmany którzy zabiją pionek: {kto_bije}')
else:
    print('żaden hetman nie zabije pionek')