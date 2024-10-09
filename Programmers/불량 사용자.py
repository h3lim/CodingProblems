import re
from itertools import product


def solution(user_id, banned_id):
    ans = set()
    lst = []

    for i in banned_id:
        pattern = re.compile(i.replace("*", "."))
        lst.append([user for user in user_id if pattern.fullmatch(user)])

    for i in product(*lst):
        if len(i) == len(set(i)):
            ans.add(tuple(sorted(i)))

    return len(ans)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])