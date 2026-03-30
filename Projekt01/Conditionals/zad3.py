# link do zadania https://exercism.org/tracks/python/exercises/pig-latin



def translate_word(word):
    vowels = "aeiou"

    if word[0] in vowels or word.startswith(("xr", "yt")):
        return word + "ay"

    if "qu" in word:
        qu_index = word.find("qu")
        before_qu = word[:qu_index]
        if all(char not in vowels for char in before_qu):
            return word[qu_index + 2:] + before_qu + "quay"

    for i in range(1, len(word)):
        if word[i] == 'y':
            before_y = word[:i]
            if all(char not in vowels for char in before_y):
                return word[i:] + before_y + "ay"
        if word[i] in vowels:
            break

    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + "ay"

    return word + "ay"


def translate(text):
    return " ".join(translate_word(word) for word in text.split())