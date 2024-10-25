def solution(scores):
    wanho = scores[0]
    N = len(scores)

    # Step 1: Check if Wanho is eligible
    for s in scores:
        if s[0] > wanho[0] and s[1] > wanho[1]:
            return -1

    # Step 2: Identify all eligible employees
    # Sort by decreasing first score, then increasing second score
    scores.sort(key=lambda x: (-x[0], x[1]))

    eligible = []
    max_second_score = -1

    for s in scores:
        if s[1] < max_second_score:
            continue  # Employee is dominated
        else:
            max_second_score = s[1]
            is_wanho = (s == wanho)
            total_score = s[0] + s[1]
            eligible.append((total_score, is_wanho))

    # Step 3: Rank the eligible employees
    eligible.sort(reverse=True)  # Sort by total score in descending order

    rank = 1
    i = 0
    while i < len(eligible):
        current_total = eligible[i][0]
        same_score_count = 1
        if eligible[i][1]:  # Check if this is Wanho
            return rank
        j = i + 1
        while j < len(eligible) and eligible[j][0] == current_total:
            if eligible[j][1]:
                return rank
            same_score_count += 1
            j += 1
        rank += same_score_count
        i = j

    # If Wanho is not found (should not happen)
    return -1


solution([[2,2],[1,4],[3,2],[3,2],[2,1]])