# link do zadania https://exercism.org/tracks/python/exercises/isogram



def is_isogram(string):
    clean_string = string.lower()
    letters = [char for char in clean_string if char.isalpha()]
    return len(letters) == len(set(letters))

print(is_isogram("lumberjacks"))
print(is_isogram("six-year-old"))
print(is_isogram("isograms"))
print(is_isogram("Alphabet"))