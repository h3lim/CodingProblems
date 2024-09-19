import math

def solution(w, h):
    k = math.gcd(w, h)
    w1, h1 = w // k, h // k

    return (w * h) - (k * (w1 + h1 - 1))