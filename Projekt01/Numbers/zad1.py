# link do zadania https://exercism.org/tracks/python/exercises/armstrong-numbers



def is_armstrong(number):
    str_num = str(number)
    power = len(str_num)

    total_sum = 0
    for digit in str_num:
        total_sum += int(digit) ** power
    return total_sum == number

print(f"9: {is_armstrong(9)}")
print(f"10: {is_armstrong(10)}")
print(f"153: {is_armstrong(153)}")