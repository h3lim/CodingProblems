from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    def bfs(b, curr, visited):
        dq = deque()
        dq.append((b, curr))

        while dq:
            currWord, currCnt = dq.popleft()

            if currWord == target:
                return currCnt
            for i in words:
                cnt = 0

                if i in visited:
                    continue
                for j in range(len(i)):
                    if currWord[j] != i[j]:
                        cnt += 1
                    if cnt > 1:
                        break
                if cnt == 1:
                    visited.add(i)
                    dq.append((i, currCnt + 1))
        return 0

    visited = set()
    visited.add(begin)
    return bfs(begin, 0, visited)