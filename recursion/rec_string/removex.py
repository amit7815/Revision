def removeX(s):
    l = len(s)
    if l == 0:
        return s

    smallOut = removeX(s[1:])

    if s[0] == 'x':
        return smallOut
    else:
        return s[0] + smallOut

s = input()
print(removeX(s))