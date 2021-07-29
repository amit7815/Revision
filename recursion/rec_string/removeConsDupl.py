'''Remove consecutive Duplicate'''

def remove(s):
    l = len(s)
    if l == 0 or l == 1:
        return s
    smallOut = remove(s[1:])
    if s[0] == smallOut[0]:
        return s[0] + smallOut[1:]   # or smallOut
    else:
        return s[0]+smallOut


s = input()
print(remove(s))