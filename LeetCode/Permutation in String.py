from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Cnt, s2Cnt = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Cnt[ord(s1[i]) - ord('a')] += 1
            s2Cnt[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1Cnt[i] == s2Cnt[i] else 0)

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            idx = ord(s2[r]) - ord('a')
            s2Cnt[idx] += 1
            if s1Cnt[idx] == s2Cnt[idx]:
                matches += 1
            elif s1Cnt[idx] + 1 == s2Cnt[idx]:
                matches -= 1
                         
            idx = ord(s2[l]) - ord('a')
            s2Cnt[idx] -= 1
            if s1Cnt[idx] == s2Cnt[idx]:
                matches += 1
            elif s1Cnt[idx] - 1 == s2Cnt[idx]:
                matches -= 1

            l += 1

        return matches == 26

Solution = Solution()

print(Solution.checkInclusion("ab", "eidboaoo"))


"""
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Cnt, s2Cnt = [0] * 26, [0] * 26

        for i in range(len(s1Cnt)):
            s1Cnt[ord(s1[i])- ord('a')] += 1
            s2Cnt[ord(s1[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if s1Cnt[i] == s2Cnt[i]:
                matches += 1
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            idx = ord(s2[r]) - ord('a')

            s2Cnt[idx] += 1

            if s1Cnt[idx] == s2Cnt[idx]:
                matches += 1
            else:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            s2Cnt[idx] -= 1

            if s1Cnt[idx] == s2Cnt[idx]:
                matches += 1
            else:
                matches -= 1
        return False
"""