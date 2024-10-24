N,K = map(int, input().split())

ans = []
lst = [i for i in range(1, N+1)]
idx = 0
while len(lst) > 0:
    idx = (idx + K-1) % len(lst)
    ans.append(lst.pop(idx))

print("<" + ", ".join(map(str,ans)) + ">")
