# link do zadania https://exercism.org/tracks/python/exercises/little-sisters-vocab



"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word

# print(add_prefix_un('manageable'))


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = " :: " + vocab_words[0]
    return prefix.join(vocab_words)

# print(make_word_groups(['un','happy','manageable','xd']))

    


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    original_root_word = word[:-4]
    if original_root_word[-1] == 'i':
        original_root_word = original_root_word[:-1] + 'y'
    return original_root_word


#print(remove_suffix_ness('sadness'))

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    adjective = sentence.split()[index]
    if adjective[-1] == '.':
        adjective = adjective[:-1]
    suffix = 'en'
    return adjective + suffix


#print(adjective_to_verb('I need to make that bright.', -1 ))
#print(adjective_to_verb('It got dark as the sun set.', 2))