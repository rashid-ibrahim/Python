"""
Problem Statement Found: https://www.hackerrank.com/challenges/the-minion-game/problem

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.
"""


def count_substrings(word):
    vowels = ['a', 'e', 'i', 'o', 'u']

    word_length = len(word)

    counts = {
        'kevin': 0,
        'stuart': 0
    }

    for letter in range(0, word_length):
        if word[letter] in vowels:
            player = 'kevin'
        else:
            player = 'stuart'

        counts[player] += word_length-letter

    return counts


def minion_game(string):
    string = string.lower()
    counts = count_substrings(string)

    if counts['stuart'] > counts['kevin']:
        print(f'Stuart {counts["stuart"]}')
    elif counts['stuart'] < counts['kevin']:
        print(f'Kevin {counts["kevin"]}')
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game('Banana')
