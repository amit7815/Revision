''' Given a Sring S , computer recursively a new string where identical chars that
are adjacent in the original string are separated from each other be * 
i.e  aaaaa--> a*a*a*a*a 
     hello --> hel*lo '''


def pair_star(s):
    ''' T -- O(N) '''
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == s[1]:
        smallOutput = pair_star(s[1:])
        return s[0] + "*" + smallOutput
    else:
        smallOutput = pair_star(s[1:])
        return s[0] + smallOutput

s = input()
print(pair_star(s))