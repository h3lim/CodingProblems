from collections import defaultdict
import math


def solution(fees, records):
    ans = []
    baseTime, baseRate = fees[0], fees[1]
    unitTime, unitRate = fees[2], fees[3]

    dic = defaultdict(list)

    for i in records:
        r = i.split()
        r[0] = r[0].replace(":", "")
        dic[r[1]].append(r[0])

    dic = defaultdict(list, {key: dic[key] for key in sorted(dic)})

    for v in dic.values():
        if len(v) % 2 == 0:
            print(v)
            time = 0
            for i in range(0,len(v), 2):
                t1 = (int(v[i + 1][:2]) * 60) + int(v[i + 1][2:])
                t2 = (int(v[i][:2]) * 60) + int(v[i][2:])
                time += t1 - t2
            if time <= baseTime:
                ans.append(baseRate)
            else:
                rate = baseRate
                rate += math.ceil((time - baseTime) / unitTime) * unitRate
                ans.append(rate)

        elif len(v) % 2 == 1:
            time = 0
            for i in range(0,len(v)-1, 2):
                t1 = (int(v[i + 1][:2]) * 60) + int(v[i + 1][2:])
                t2 = (int(v[i][:2]) * 60) + int(v[i][2:])
                time += t1 - t2
            t1 = 1439
            t2 = (int(v[-1][:2]) * 60) + int(v[-1][2:])
            time += t1 - t2
            if time <= baseTime:
                ans.append(baseRate)
            else:
                rate = baseRate
                rate += math.ceil((time - baseTime) / unitTime) * unitRate
                ans.append(rate)

        print(ans)


solution([1, 461, 1, 10],["00:00 1234 IN"]	)