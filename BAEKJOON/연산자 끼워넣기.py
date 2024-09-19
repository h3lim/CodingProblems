import math
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

plus,subs,multi,divide = map(int, sys.stdin.readline().split())
mx,mn = float("-inf"), float("inf")
def dfs(i,p,s,m,d, t):
    global mx, mn

    if i == len(numbers):
        mx = max(mx,t)
        mn = min(mn,t)
        return

    if p > 0:
        dfs(i+1,p-1,s,m,d,(t + numbers[i]))
    if s > 0:
        dfs(i + 1, p, s-1, m, d, (t - numbers[i]))
    if m > 0:
        dfs(i + 1, p, s, m-1, d, (t * numbers[i]))
    if d > 0:
        if t >= 0:
            dfs(i + 1, p, s, m , d-1, (math.floor(t / numbers[i])))
        else:
            dfs(i + 1, p, s, m, d - 1, (-math.floor(-t / numbers[i])))
dfs(1,plus,subs,multi,divide, numbers[0])

print(mx,mn)