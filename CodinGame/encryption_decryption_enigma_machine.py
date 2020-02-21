import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def gen_map(alpha, shift_by, message):
    map_key = []
    for _ in message:
        # print(f'shift_by: {shift_by}', file=sys.stderr)
        map_key.append(alpha[shift_by])
        if shift_by == 25:
            shift_by = 0
        else:
            shift_by += 1

    print(f'map_key: {"".join(map_key)}', file=sys.stderr)
    return ''.join(map_key)


def unmap(alpha, shift_by, message):
    map_key = []
    alpha = alpha[::-1]
    print(f'alpha: {alpha}', file=sys.stderr)
    for _ in message:
        map_key.append(alpha[shift_by])
        if shift_by == 25:
            shift_by = 0
        else:
            shift_by += 1

    return ''.join(map_key)


def encrypt(message, alpha, rotor):
    merged = dict(zip(alpha, rotor))
    out = []
    print(f'message: {message}', file=sys.stderr)
    print(f'merged: {merged}', file=sys.stderr)
    for i in message:
        out.append(merged[i])

    print(f'encrypted out: {"".join(out)}', file=sys.stderr)
    return ''.join(out)


def decrypt(message, alpha, rotor):
    merged = dict(zip(rotor, alpha))
    out = []
    for i in message:
        out.append(merged[i])

    print(f'encrypted out: {"".join(out)}', file=sys.stderr)
    return ''.join(out)


def main():
    operation = input()
    pseudo_random_number = int(input())
    rotor_list = []
    for _ in range(3):
        rotor = input()
        rotor_list.append(rotor)
    message = input()

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print(f'operation: {operation}', file=sys.stderr)

    if operation == 'encrypt':
        result = gen_map(alpha, pseudo_random_number, message)

        for curr_rotor in rotor_list:
            result = encrypt(result, alpha, curr_rotor)
    else:
        result = unmap(alpha, pseudo_random_number, message)

        for curr_rotor in rotor_list:
            result = decrypt(result, alpha, curr_rotor)

    print(result)
    # print(f'result: {result}', file=sys.stderr)
    # print(f'number: {pseudo_random_number}, rotor: {rotor}, rotor_list: {rotor_list},
    # operation: {operation}, message: {message}, caesar_shift: {caesar_shift}', file=sys.stderr)


main()

# print("message")