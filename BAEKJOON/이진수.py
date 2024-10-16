N = int(input())

for i in range(N):
    tmp = list(bin(int(input()))[2:])
    tmp.reverse()
    for j in range(len(tmp)):
        if tmp[j] == "1":
            print(j, end = " ")

    print()

