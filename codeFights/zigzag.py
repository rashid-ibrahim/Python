
def flipCheck(n1, n2):
    if n1 == n2:
        return 0
    elif n1 > n2:
        return 1
    elif n1 < n2:
        return 2


def checkVal(flip, n1, n2):
    if flip == 1:
        if n1 > n2:
            return 1
        else:
            return 2
    else:
        if n1 < n2:
            return 1
        else:
            return 2


def zigzag(a):
    if len(a) == 2 and a[0] == a[1]:
        return 1
    elif len(a) == 2:
        return 2

    
    mSequences = []
    start = 0

    flip = flipCheck(a[0],a[1])
    if flip == 0:
        mSequences.append(a[0],[a1])
        start = 1
        
    cur = []
    for i in range(start, len(a)-1):
        if a[i] == a[i+1] or a[i] == a[i-1]:
            i += 1
        else:
            if len(cur)==0:
                flip = flipCheck(a[i], a[i+1])
                if flip == 0:
                    mSequence.append([a[i],a[i+1]])
                    i += 1
                else:
                    cur.append(a[i])
            else:
                cv = checkVal(flip, cur[len(cur)-1], a[i])
                if cv != 1:
                    mSequences.append(cur)
                    cur = []
                cur.append(a[i])

            flip = flipCheck(a[i], a[i+1])

            if len(cur) > 3:
                #print('cur: {0}'.format(cur))
                #print('cur details: {0}, {1}'.format(cur[-4:-2], cur[-2:]))
                #print(cur[-4] == cur[-2])
                if cur[-4] == cur[-2] and cur[-3] == cur[-1]:
                    #print('break')
                    cur.pop()
                    mSequences.append(cur)
                    cur = []

    #appends the final cur value
    mSequences.append(cur)
    long = 0

    for i in range(0, len(mSequences)):
        if len(mSequences[i]) > long:
            long = len(mSequences[i])
            
    return long


9, 8, 8, 5, 3, 5, 3, 2, 8, 6
n = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6]
print(zigzag(n))
n = [2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4]
2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4
print(zigzag(n))
