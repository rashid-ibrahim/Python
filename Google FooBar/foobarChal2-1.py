
def chainBuild(*iterables):
    r = []
    for it in iterables:
        for element in it:
            r.append(element)
    return r
            
def answer(xs):
    if len(xs) == 1:
        return str(xs[0])
    neg,pos,absNeg = [x for x in xs if x < 0], [x for x in xs if x > 0], [abs(x) for x in xs if x < 0]
    
    neg.sort()
    
    if len(neg)%2 == 1:
        absNeg.pop(absNeg.index(abs(neg[-1])))
        neg = neg[:-1]

    out = sorted(pos + absNeg,key=int,reverse=True)
    
    if len(out) > 3:
        out = out[0:3]   
    ans = 1

    allFound = True
    for i in absNeg:
        try:
            out.index(i)
        except ValueError:
            allFound = False

    if allFound == True:
        for i in out:
            ans *= i
    else:
        for i in pos[0:3]:
            ans *= i
    
    return str(ans)

x = list(map(int,[2, -1, 2, 10, -11]))
an = answer(x)
print('The answer is {0}'.format(an))
print(type(an))
