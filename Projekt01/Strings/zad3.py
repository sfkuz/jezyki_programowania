# link do zadania https://exercism.org/tracks/python/exercises/pangram



def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    sentence_lower = sentence.lower()

    for char in alphabet:
        if char not in sentence_lower:
            return False
    return True

print(is_pangram("brown"))
print(is_pangram("The quick brown fox jumps over the lazy dog."))   