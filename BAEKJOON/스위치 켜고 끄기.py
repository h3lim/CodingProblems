N = int(input())

lst = list(map(int, input().split()))
lst.insert(0,0)
M = int(input())

genNum = []

for _ in range(M):
    genNum.append(list(map(int, input().split())))

for g,n in genNum:
    if g == 1:
        num = 1
        while n * num <= N:
            if lst[n * num] == 1:
                lst[n * num] = 0
            else:
                lst[n * num] = 1
            num += 1
    else:
        if lst[n] == 1:
            lst[n] = 0
        else:
            lst[n] = 1
        left, right = n-1, n+1
        while left > 0 and right < N+1:
            if lst[left] == lst[right]:
                if lst[left] == 1:
                    lst[left] = 0
                    lst[right] = 0
                else:
                    lst[left] = 1
                    lst[right] = 1
            else:
                break
            left -= 1
            right += 1


for i in range(1,len(lst),20):
    print(" ".join(map(str,lst[i:i+20])))
