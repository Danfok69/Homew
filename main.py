# Вариант 1

def compound_match(words, target):
    a = [i for i in range(len(words)) if words[i] in target]
    for i in range(len(a)):
        if target.replace(words[a[i-1]], "") == words[a[i]]:
            b = [words[a[i-1]], words[a[i]]]
    c = [i for i in (b if b[0] + b[1] == target else b[::-1])]
    c.append([words.index(c[0]), words.index(c[1])])
    print(a, b, c)
    return c

# Вариант 2

def compound_match(words, target):
    a = [i for i in range(len(words)) if words[i] in target]
    for i in range(len(a)):
        if target.replace(words[a[i-1]], "") == words[a[i]]:
            b = [words[a[i-1]], words[a[i]]]
        else:
            return None    
    c = [i for i in (b if b[0] + b[1] == target else b[::-1])]
    d = [words.index(c[0]), words.index(c[1])]
    e = [i for i in words if i in c]
    e.append(d)
    return e
