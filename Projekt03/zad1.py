import random
import unittest

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

plansza = [['.' for j in range(cols)] for i in range(rows)]

def losowanie_hetmanow(plansza, k_position, k):
    while len(k_position) < k:
        r = random.randint(0, 7)
        c = random.randint(0, 7)
        if plansza[r][c] == '.':
            plansza[r][c] = 'H'
            k_position.append((r, c))

losowanie_hetmanow(plansza, k_position, k)

def losowanie_pionka(plansza, p_position):
    while True:
        rp = random.randint(0, 7)
        cp = random.randint(0, 7)
        if plansza[rp][cp] == '.':
            plansza[rp][cp] = 'P'
            p_position.append((rp, cp))
            break

losowanie_pionka(plansza,p_position)

def wyswietlenie_planszy(plansza):
    for row in plansza:
        print(" ".join(row))

wyswietlenie_planszy(plansza)


# ZADANIE 2

def atak(p_position, k_position):
    kto_bije = []
    pr, pc = p_position[0]  # pozycja pionka w linijce i kolumnie

    for h in k_position:
        hr, hc = h  # pozycja hetmana w linijce i kolumnie
        if (hr == pr) or (hc == pc) or (abs(hr - pr) == abs(hc - pc)):  # abs żeby liczba nie była ujemna
            kto_bije.append(h)
    return kto_bije

class TestAtak(unittest.TestCase):
    def test_atak_po_ziomie(self):
        self.assertEqual(len(atak([(4, 4)], [(4, 0)])), 1)
    def test_atak_po_pionie(self):
        self.assertEqual(len(atak([(4, 4)], [(0, 4)])), 1)
    def test_atak_po_diagonali(self):
        self.assertEqual(len(atak([(4, 4)], [(6, 6)])), 1)
    def test_brak_ataku(self):
        self.assertEqual(len(atak([(4, 4)], [(0, 1)])), 0)

wynik = atak(p_position, k_position)

if wynik:
    print(f'hetmany którzy zabiją pionek: {wynik}')
else:
    print('żaden hetman nie zabije pionek')

# ZADANIE 3

while True:
    print('\n===Co chcesz zrobić?===')
    print('1. losuj nową pozycje pionka')
    print('2. usuń hetmana')
    print('3. Wyjdź')
    print('4. uruchom testy')

    wybor = input('podaj wybór: ')

    if wybor == '1':
        old_r, old_c = p_position[0]
        plansza[old_r][old_c] = '.'
        p_position.clear()
        losowanie_pionka(plansza, p_position)
    elif wybor == '2':
        while True:
            r_del = int(input('linijka do usunięcia(0-7): '))
            c_del = int(input('kolumna do usunięcia(0-7): '))
            if r_del < 8 and c_del < 8:
                if (r_del, c_del) in k_position:
                    plansza[r_del][c_del] = '.'
                    k_position.remove((r_del, c_del))
                    print('Hetman został usunięty.')
                    break
                else:
                    print('Na tej pozycji nie ma hetmana! Spróbuj ponownie.')
            else:
                print('Liczba musi być od 0 do 7. Spróbuj ponownie.')
    elif wybor == '3':
        break
    elif wybor == '4':
        print("\n--- URUCHAMIANIE TESTÓW ---")
        unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestAtak))

    wyswietlenie_planszy(plansza)
    wynik = atak(p_position, k_position)

    if wynik:
        print(f'hetmany którzy zabiją pionek: {wynik}')
    else:
        print('żaden hetman nie zabije pionek')