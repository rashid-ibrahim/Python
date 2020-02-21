def first_non_repeating_letter(string):
    if string == '':
        return ''
    if len(string) == 1:
        return string

    string_lower = string.lower()

    for i in range(0, len(string)):
        if string_lower.count(string_lower[i]) == 1:
            return string[i]

    return ''


x = first_non_repeating_letter('moonmen')
print(x)
