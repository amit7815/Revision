def replaceab(s):
    l = len(s)
    if l==0:
        return s
    smallOut = replaceab(s[1:])
    if s[0] == 'a':
        return 'b' + smallOut
    else:
        return smallOut

s = input()
print(replaceab(s))