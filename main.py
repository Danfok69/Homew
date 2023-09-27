def compound_match(words, target):
    a = [i for i in range(len(words)) if words[i] in target]
    for i in range(len(a)):
        if target.replace(words[a[i-1]], "") == words[a[i]]:
            b = [words[a[i-1]], words[a[i]]]
    c = [i for i in (b if b[0] + b[1] == target else b[::-1])]
    c.append([words.index(c[0]), words.index(c[1])])
    print(a, b, c)
    return c
