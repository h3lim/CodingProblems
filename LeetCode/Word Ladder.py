from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def bfs(b, curr, visited):
            dq = deque()
            dq.append((b, curr))

            while dq:
                currWord, currCnt = dq.popleft()

                if currWord == endWord:
                    return currCnt

                for i in wordList:
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
        visited.add(beginWord)
        return bfs(beginWord, 1, visited)