"""
Problem Statement Found At: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""


def pos_to_char_map():
    return [chr(pos + 97) for pos in range(0, 26)]


def designerPdfViewer(h, word):
    alpha_map = pos_to_char_map()

    max_val = -1

    for i in word:
        val = h[alpha_map.index(i)]

        if val > max_val:
            max_val = val

    return max_val * len(word)


if __name__ == '__main__':
    def gen_list(s): return [int(x) for x in s.split(' ')]

    test_cases = [
        (gen_list('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'), 'abc', 9),
        (gen_list('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'), 'zaba', 28)
    ]

    for case in test_cases:
        answer = designerPdfViewer(case[0], case[1])

        print(answer == case[2])
