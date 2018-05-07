

def main(d):
    out = {}
    #for k, v in d.items(): print (k, '>', v)
    for k, v in d.items():
        for x in v:
            if x in out:
                out[x].append(k)
            else:
                out[x] = []
                out[x].append(k)
    return out


if __name__ == '__main__':
    d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
    out = main(d)
    print(out)
