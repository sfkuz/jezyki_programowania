import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

start = int(input('Podaj początek zakresu: '))
end = int(input('Podaj koniec zakresu: '))

print(f'liczby pierwsze od {start} do {end}:')

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")