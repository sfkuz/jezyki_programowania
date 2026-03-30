# link do zadania https://exercism.org/tracks/python/exercises/grains



def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1

print(square(5))
print(total())