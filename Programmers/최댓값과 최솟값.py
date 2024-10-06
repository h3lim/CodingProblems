def solution(s):
    return " ".join([str(min(map(int, s.split()))),str(max(map(int, s.split())))])