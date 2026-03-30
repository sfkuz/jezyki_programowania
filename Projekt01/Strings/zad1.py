# link do zadania https://exercism.org/tracks/python/exercises/isbn-verifier



def is_valid(isbn):
    digits = isbn.replace("-", "")

    if len(digits) != 10:
        return False

    total_sum = 0

    for i in range(10):
        char = digits[i]

        if i == 9 and char == 'X':
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total_sum += value * (10 - i)

    return total_sum % 11 == 0

print(is_valid("3-598-21508-8"))
print(is_valid("3-598-21507-X"))
print(is_valid("3598215088"))
print(is_valid("3-598-21507-A"))