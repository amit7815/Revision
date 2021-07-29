'''Convert a Numeric String into integer string i.e '1234'--> 1234 '''

def stringToInteger(s):
    if len(s) == 1:
        return int(s)
    return int(s[0])*(10**(len(s)-1)) + stringToInteger(s[1:])

s  = input()
print(stringToInteger(s), type(stringToInteger(s)))