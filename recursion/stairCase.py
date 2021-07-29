''' A child is running up a staircase with N steps and can hop either 1 step, 2 step
or 3 step at a time . implement a method yo count howmany possible ways the child can
run up to the stairs . You need to return no of possible ways w'''

def stairCase(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    ans1 = stairCase(n-1)
    ans2 = stairCase(n-2)
    ans3 = stairCase(n-3)

    return ans1 + ans2 + ans3

n = int(input())
print(stairCase(n))