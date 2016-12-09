import os, sys, string

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
    best_score = 0
    best_word = ''
    for letter in letters:
        if letters[letter] > 0:
            letters[letter] -= 1
            actual_word += letter
            next_letters = string.ascii_lowercase if letter == '?' else [letter]
            for child in next_letters:
                word += child
                if child in node['children']:
                    if node['children'][child]['isWord'] and score(actual_word) > best_score:
                        best_score, best_word = score(actual_word), word
                    next_score, next_word = dfs(node['children'][child], letters, score, word, actual_word)
                    if next_score > best_score:
                        best_score, best_word = next_score, next_word
                word = word[:-1]
            actual_word = actual_word[:-1]
            letters[letter] += 1
    return best_score, best_word


def highest(dictionary, letters):
    letter_counts = {}
    for i in list(letters):
        letter_counts[i] = letter_counts.get(i, 0) + 1
    best_score, best_word = dfs(dictionary, letter_counts, score)
    print('"{}" -> {}, "{}"'.format(letters, best_score, best_word))

def handle(lines):
    dictionary = load_dictionary("enable1.txt")
    for line in [line.strip() for line in lines if len(line.strip())]:
        highest(dictionary, line)

handle(sys.stdin.readlines())
