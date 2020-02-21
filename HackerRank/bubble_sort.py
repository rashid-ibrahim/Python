

def countSwaps(a):
    size = len(a)
    count = 0
    for i in range(0, size):
        for j in range(0, size-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
    return count


x = countSwaps([3, 2, 1])
print(x)
