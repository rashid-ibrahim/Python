
def chainBuild(*iterables):
    for it in iterables:
        for element in it:
            yield element

def answer(xs):
    neg,pos, absNeg = [x for x in xs if x < 0], [x for x in xs if x > 0], [abs(x) for x in xs if x < 0]
    if len(xs) == 1 or not pos and not neg:
        return xs
    
    neg.sort()
    
    print('absNeg1: {0}'.format(absNeg))
    print('neg: {0}'.format(neg))
    print('abs(neg[-1]: {0}'.format(abs(neg[-1])))
    if len(neg)%2 == 1:
        absNeg.pop(absNeg.index(abs(neg[-1])))
        neg = neg[:-1]
    #print('absNeg2: {0}'.format(absNeg))
    out = []
    i = 0
    pos = sorted(pos, key=int, reverse=True)
    absNeg = sorted(absNeg, key=int, reverse=True)
    erno = sorted(pos + absNeg,key=int,reverse=True)
    print('absNeg: {0}'.format(absNeg))
    print('pos: {0}'.format(pos))
    print('erno: {0}'.format(erno))
    
    '''or x in chainBuild(pos, absNeg):
        if i >= 3:
            break
        i+= 1
        out.append(x)
'   '''
    if len(erno) > 3:
        erno = erno[0:3]
    
    print('erno2: {0}'.format(erno))   
    ans = 1
    for i in erno:
        ans *= i
    
    
    return ans

x = list(map(int,[2, -3, 4, -5, 16, -22, 10, 12]))
an = answer(x)
print('The answer is {0}'.format(an))
print(type(an))
