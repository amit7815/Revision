def replacePI(s):
    l = len(s)
    if l == 0 or l== 1:
        return s
    smallOut = replacePI(s[1:])
    if s[0] =='p' and smallOut[0] == 'i':
        return '3.14' + smallOut[1:]
    else:
        return s[0] + smallOut


s = input()
print(replacePI(s))