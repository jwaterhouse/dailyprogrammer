import string

def insert(node, value, index = 0):
    if not value[index] in node['children']:
        node['children'][value[index]] = {'children': {}, 'isWord': False}
    if index + 1 == len(value):
        node['children'][value[index]]['isWord'] = True
    elif index + 1 < len(value):
        insert(node['children'][value[index]], value, index + 1)

def load_dictionary(filepath):
    root = {'children': {}, 'isWord': False}
    with open(filepath) as f:
        for line in f.readlines():
            insert(root, list(line.strip()))
    return root

def score(word):
    points = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
    score = 0
    for i in range(0, len(word)):
        score += (i + 1) * points[ord(word[i]) - ord('a')] if word[i] != '?' else 0
    return score

def dfs(node, letters, score, word = '', actual_word = ''):
    best_score, best_word, best_actual_word = 0, '', ''
    for letter in letters:
        if letters[letter] > 0:
            letters[letter] -= 1
            actual_word += letter
            next_letters = string.ascii_lowercase if letter == '?' else [letter]
            for child in next_letters:
                word += child
                if child in node['children']:
                    if node['children'][child]['isWord'] and score(actual_word) > best_score:
                        best_score, best_word, best_actual_word = score(actual_word), word, actual_word
                    next_score, next_word, next_actual_word = dfs(node['children'][child], letters, score, word, actual_word)
                    if next_score > best_score:
                        best_score, best_word, best_actual_word = next_score, next_word, next_actual_word
                word = word[:-1]
            actual_word = actual_word[:-1]
            letters[letter] += 1
    return best_score, best_word, best_actual_word


def count_letters(letters):
    letter_counts = {}
    for i in list(letters):
        letter_counts[i] = letter_counts.get(i, 0) + 1
    return letter_counts

def remove_letters_from_word(letters, word):
    for w in word:
        letters = letters.replace(w, '', 1)
    return letters

def check(dictionary, tiles, num_tiles = 10):
    letters = ''
    total_score = 0
    while True:
        best_choice, best_score, best_word, best_actual_word, best_letters = 0, 0, '', '', ''
        num_to_choose = min(num_tiles - len(letters), len(tiles))
        for i in range(0, num_to_choose + 1):
            chosen_letters = letters + tiles[0:i] + tiles[len(tiles)-(num_to_choose - i):]
            next_score, next_word, next_actual_word = dfs(dictionary, count_letters(chosen_letters), score)
            if next_score > best_score:
                best_choice, best_score, best_word, best_actual_word, best_letters = i, next_score, next_word, next_actual_word, chosen_letters
        total_score += best_score
        letters = best_letters
        tiles = tiles[best_choice:len(tiles) - (num_to_choose - best_choice)]
        letters = remove_letters_from_word(letters, best_actual_word)
        if best_word != '':
            print('{} {} {}'.format(best_choice, best_actual_word, best_word, letters))
        if best_word == '' or len(tiles) == 0:
            break

_DICTIONARY = load_dictionary("enable1.txt")

check(_DICTIONARY, "sd?zeioao?mluvepesceinfxt?wyiru?ie?giator?t??nuefje?l?odndrotpewlgoobiinysagacaqski?aeh?rbhaervtnl?m")
