def towerOfHanoi(n, a, b, c):
    ''' T--O(2^n) , NO of moves = 2^n - 1 '''
    if n==1:
        print('move 1st disk from ',a ,"to", c)
        return

    towerOfHanoi(n-1, a, c, b)
    print("move", n,"th disk from ",a , 'to ', c)
    towerOfHanoi(n-1, b, a, c)

n = int(input())
towerOfHanoi(n, 's', 'h', 'd')