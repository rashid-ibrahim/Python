"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-2d-arrays/problem
"""


def hour_glass_map(arr):
    output = []

    for i in range(4):
        for j in range(4):
            temp = []
            # Top line of the hour glass
            temp.append(arr[i][j])
            temp.append(arr[i][j+1])
            temp.append(arr[i][j+2])
            # Middle line of the hour glass
            temp.append(arr[i+1][j+1])
            # Bottom line of the hour glass
            temp.append(arr[i+2][j])
            temp.append(arr[i+2][j+1])
            temp.append(arr[i+2][j+2])

            output.append(temp)

    return output


def main(arr):
    my_map = hour_glass_map(arr)

    largest = sum(my_map[0])
    for i in my_map:
        cur = sum(i)
        if cur > largest:
            largest = cur

    print(largest)
