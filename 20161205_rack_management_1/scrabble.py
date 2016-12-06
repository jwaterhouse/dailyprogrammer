import sys, string

def scrabble(letters, word):
    letters = list(letters)
    word = list(word)
    for w in range(len(word)):
        found = False
        for l in range(len(letters)):
            if word[w] == letters[l] or letters[l] == '?':
                letters[l] = '\0'
                found = True
                break
        if not found:
            return False
    return True

def load_dictionary(filepath):
    lines = []
    with open(filepath) as f:
        lines = [l.strip() for l in f.readlines() if len(l.strip()) > 0]
    lines.sort()
    return lines

def has_word(dictionary, word):
    return binary_search(dictionary, word, lambda x, y: x == y)

def has_word_prefix(dictionary, word):
    return binary_search(dictionary, word, lambda x, y: x.startswith(y))

def binary_search(dictionary, word, found_fn):
    first = 0
    last = len(dictionary) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if found_fn(dictionary[midpoint], word):
            found = True
        elif word < dictionary[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found

def depth_first_search(dictionary, letters, word, comparison):
    best_word = ""
    for l in letters.keys():
        if letters[l] != 0:
            letters[l] -= 1
            letters_to_check = (string.ascii_lowercase if l == '?' else list(l))
            for nl in letters_to_check:
                word.append(nl)
                if has_word(dictionary, "".join(word)) and comparison(word, best_word):
                    best_word = "".join(word)
                if has_word_prefix(dictionary, "".join(word)):
                    next_word = depth_first_search(dictionary, letters, word, comparison)
                    if comparison(next_word, best_word):
                        best_word = next_word
                word.pop()
            letters[l] += 1
    return best_word

def longest(dictionary, letters):
    letter_counts = {}
    for i in list(letters):
        letter_counts[i] = letter_counts.get(i, 0) + 1
    return depth_first_search(dictionary, letter_counts, list(), lambda x, y: len(x) > len(y))

def score(word):
    points = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q':10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    return sum(points[letter] for letter in word)

def highest(dictionary, letters):
    letter_counts = {}
    for i in list(letters):
        letter_counts[i] = letter_counts.get(i, 0) + 1
    return depth_first_search(dictionary, letter_counts, list(), lambda x, y: score(x) > score(y))

print("Challenge:")
print(scrabble("ladilmy", "daily"))
print(scrabble("eerriin", "eerie"))
print(scrabble("orrpgma", "program"))
print(scrabble("orppgma", "program"))
print("")

print("Bonus 1:")
print(scrabble("pizza??", "pizzazz"))
print(scrabble("piizza?", "pizzazz"))
print(scrabble("a??????", "program"))
print(scrabble("b??????", "program"))
print("")

_DICTIONARY = load_dictionary("enable1.txt")

print("Bonus 2:")
print(longest(_DICTIONARY, "dcthoyueorza"))
print(longest(_DICTIONARY, "uruqrnytrois"))
print(longest(_DICTIONARY, "rryqeiaegicgeo??"))
print(longest(_DICTIONARY, "udosjanyuiuebr??"))
print(longest(_DICTIONARY, "vaakojeaietg????????"))
print("")

print("Bonus 3:")
print(highest(_DICTIONARY, "dcthoyueorza"))
print(highest(_DICTIONARY, "uruqrnytrois"))
print(highest(_DICTIONARY, "rryqeiaegicgeo??"))
print(highest(_DICTIONARY, "udosjanyuiuebr??"))
print(highest(_DICTIONARY, "vaakojeaietg????????"))
print("")
