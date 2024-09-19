import sys

N = int(sys.stdin.readline())

l = list(sys.stdin.readline().rstrip())
ans = float("-inf")
def addParenthesis(i,val):
    global ans
    if i ==  N:
        ans = max(ans,int(val))
        return

    if i + 4 <= N:
        addParenthesis(i+4, str(eval(''.join([val, l[i]] + [str(eval(''.join(l[i+1:i+4])))]))))
    if i + 2 <= N:
        addParenthesis(i+2,str(eval("".join([val] + l[i:i+2]))))


addParenthesis(1, l[0])
print(ans)