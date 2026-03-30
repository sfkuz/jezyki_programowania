# link do zadania https://exercism.org/tracks/python/exercises/rotational-cipher



def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            new_char_code = (ord(char) - start + key) % 26 + start
            result += chr(new_char_code)
        else:
            result += char

    return result

print(rotate("omg", 5))
print(rotate("Cool", 26))
print(rotate("The quick brown fox jumps over the lazy dog.", 13))
