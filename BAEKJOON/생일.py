N = int(input())

y,o = ["A","-1","-1","-1"], ["A","31","12","2011"]

for i in range(N):
    data = input().split()
    if int(data[-1]) > int(y[-1]):
        y = data
    elif int(data[-1]) == int(y[-1]):
        if int(data[-2]) > int(y[-2]):
            y = data
        elif int(data[-2]) == int(y[-2]):
            if int(data[-3]) > int(y[-3]):
                y = data
    if int(data[-1]) < int(o[-1]):
        o = data
    elif int(data[-1]) == int(o[-1]):
        if int(data[-2]) < int(o[-2]):
            o = data
        elif int(data[-2]) == int(o[-2]):
            if int(data[-3]) < int(o[-3]):
                o = data

print(y[0])
print(o[0])