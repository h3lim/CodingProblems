def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

N, K = map(int, input().split())

print(factorial(N) // (factorial(N-K) * factorial(K)))