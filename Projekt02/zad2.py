import math

def sum(n):
    if n < 2:
        return 0
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
    return total

start = int(input('Podaj początek zakresu: '))
end = int(input('Podaj koniec zakresu: '))

print(f'Zaprzyjaźnione liczby od {start} do {end}')

for a in range(start, end + 1):
    b = sum(a)
    if b > a and sum(b) == a:
        print(f'{a} i {b}')