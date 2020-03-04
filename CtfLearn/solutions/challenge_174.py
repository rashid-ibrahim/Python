"""
Challenge located at: https://ctflearn.com/challenge/174

The dat file, obtained from a link on the challenge site, is located in a different directory at the same level as this
solution.
"""


def calc_zeros(line):
    zeros = 0

    for i in line:
        if i == '0':
            zeros += 1

    if zeros % 3 == 0:
        return True

    return False


def calc_ones(line):
    ones = 0

    for i in line:
        if i == '1':
            ones += 1

    if ones % 2 == 0:
        return True

    return False


def main(file_location):

    line_count = 0

    with open(file_location) as file:
        for line in file:
            line = line.strip('\n')

            if calc_zeros(line) or calc_ones(line):
                line_count += 1

        return line_count


if __name__ == '__main__':
    print(main('../supportFiles/challenge_174.dat'))