def solution(n):
    num = n + 1
    n = bin(n)
    numOne = len(n.replace("0", ""))

    while True:
        if numOne == len(bin(num).replace("0", "")):
            return num

        num += 1