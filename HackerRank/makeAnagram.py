
def makeAnagram(a, b):
    if a == b[::-1]:
        return 0

    removed = 0

    # brute force first attempt
    looper = list(a)
    cleaned_a, cleaned_b, dirty_a, dirty_b = [], [], [], []
    while looper:
        x = looper.pop()
        if x not in b:
            removed += 1
            dirty_a.append(x)
        else:
            cleaned_a.append(x)


    looper = list(b)
    while looper:
        x = looper.pop()
        if x not in a:
            removed += 1
            dirty_b.append(x)
        else:
            cleaned_b.append(x)

    cleaned_a, cleaned_b, dirty_a, dirty_b = ''.join(cleaned_a), ''.join(cleaned_b), ''.join(dirty_a), ''.join(dirty_b)

    return removed


res = makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')
print(res)
