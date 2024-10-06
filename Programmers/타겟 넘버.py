def solution(numbers, target):
    def dfs(curr,i):
        nonlocal ans
        if i == len(numbers):
            if curr == target:
                ans += 1
            return
        dfs(curr + numbers[i], i+1)
        dfs(curr - numbers[i], i+1)
    ans = 0
    dfs(0,0)
    return ans