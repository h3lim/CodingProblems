def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, v in enumerate(nums):
        if v in s:
            s = s.replace(v, str(i))

    return int(s)