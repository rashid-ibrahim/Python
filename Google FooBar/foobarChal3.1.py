from __future__ import division
from operator import mul
from itertools import compress
from itertools import starmap
import fractions

def probDistribution(m):
    out = m[0]
    for i in range(100):
        nr = [sum(starmap(mul, zip(m[0], col))) for col in zip(*m)]
        out = nr
    return out

def calcProbabilities(m):
    pM = []

    for i in range(len(m)):
        newRow = []
        rowSum = sum(m[i])
        
        if all([v == 0 for v in m[i]]):
            for j in m[i]:
                newRow.append(0)
            newRow[i] = 1
            pM.append(newRow)
        else:
            for j in m[i]:
                if j == 0:
                    newRow.append(0)
                else:
                    newRow.append(j / sum(m[i]))
            pM.append(newRow)
    return pM

def answer(m):
    if len(m) == 1:
        return [1, 1]

    pM = calcProbabilities(m)
    
    termStates = []
    for r in range(len(m)):
        if all(x == 0 for x in m[r]):
            termStates.append(True)
        else:
            termStates.append(False)
            
    pM = probDistribution(pM)
    denominators = []

    numerators = []
    for i in pM:
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)
        denominator = fractions.Fraction(i).limit_denominator().denominator
        denominators.append(denominator)

    numeratorsTimesFactors = [a * b for a, b in zip(numerators, [max(denominators) / x for x in denominators])]
    termNumerators = list(compress(numeratorsTimesFactors, termStates))
    
    answerlist = []
    for i in termNumerators:
        answerlist.append(i)
    answerlist.append(max(denominators))

    return list(map(int, answerlist))


m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
print(answer(m))
