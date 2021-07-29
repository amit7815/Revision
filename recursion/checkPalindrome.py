def checkPalindrome(s, si, ei):
    ''' T-->O(N) '''
    if si >= ei:
        return True
    
    if s[si] == s[ei]:
        si = si + 1
        ei = ei - 1
        smalloutput = checkPalindrome(s, si, ei)
        return smalloutput
    else:
        return False


s = input()
n = len(s)
print(checkPalindrome(s, 0, n-1))
