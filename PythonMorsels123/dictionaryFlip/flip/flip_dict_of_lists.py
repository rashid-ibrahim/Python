from collections import OrderedDict

def flip_dict_of_lists(d, dict_type=None, key_func=None):
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


'''if __name__ == '__main__':
    d = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
    out = main(d)
    print(out)'''
