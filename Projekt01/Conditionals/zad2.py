# link do zadania https://exercism.org/tracks/python/exercises/matching-brackets



def is_paired(input_string):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in input_string:
        if char in pairs.values():
            stack.append(char)

        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0