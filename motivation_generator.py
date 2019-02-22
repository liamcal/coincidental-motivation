from collections import defaultdict
from random import choice
import sys
import re 

upper_re = re.compile(r'^[A-Z]+$')

def _build_dict(filepath):
    word_scores = defaultdict(list)
    with open(filepath) as f:
        for line in f:
            word = line.strip().upper()
            if (upper_re.match(word)):
                score = _score_letters(word)
                word_scores[score].append(word)
    return word_scores

def _score_letters(word):
    return sum(ord(letter) - ord('A') + 1 for letter in word)

def _random_word(word_scores, score):
    return choice(word_scores[score])

def generate_motivation(word_scores):
    random_words = [_random_word(word_scores, i) for i in [96, 98, 100]]
    return f'{random_words[0]} = 96% and {random_words[1]} = 98%.\nBut {random_words[2]} = 100%!'

def print_lists(word_scores, *scores):
    for score in scores:
        print(str(score) + ':')
        for word in word_scores[score]:
            print('\t' + word)

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'words/words.txt'
    word_scores = _build_dict(filepath)
    print(generate_motivation(word_scores))
    prompt = input()
    while not prompt.startswith('q'):
        print(generate_motivation(word_scores))
        prompt = input()