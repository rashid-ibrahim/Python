
def decrypt(raw_in):
    PASS_THROUGH =['.', ',', '\'', '"']

    ALPHA = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    ALPHA2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    mixins = []

    curr = ALPHA

    for i in range(26):
        curr = [curr[-1]] + curr[:-1]
        mixins.append(''.join(curr))

    possible_outs = []
    raw_in = raw_in.split(' ')

    count1 = -1
    for cipher_alpha in mixins:
        count1 += 1
        possible_outs.append([])
        count2 = -1
        for word in raw_in:
            count2 += 1
            possible_outs[count1].append([])
            for cipher_letter in word:
                if cipher_letter in PASS_THROUGH:
                    possible_outs[count1][count2].append(cipher_letter)
                else:
                    loc = ALPHA2.find(cipher_letter)
                    possible_outs[count1][count2].append(cipher_alpha[loc])

            possible_outs[count1][count2] = ''.join(possible_outs[count1][count2])

            print('wait')

        possible_outs[count1] = ' '.join(possible_outs[count1])

    return possible_outs


def read_in(file=None):
    if not file:
        file = '../supportFiles/Substitution.txt'

    txt = open(file).read()

    return txt


def main():

    txt = read_in()

    vals = decrypt(txt)

    return vals


if __name__ == '__main__':
    decrypt_arr = main()
    print(f'Find it: {decrypt_arr}')
