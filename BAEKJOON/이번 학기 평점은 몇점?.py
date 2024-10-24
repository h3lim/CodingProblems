N = int(input())
grade_to_score = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

total_grade = 0
total_unit = 0

for i in range(N):
    data = input().split()
    total_unit += int(data[1])
    total_grade += int(data[1]) * grade_to_score[data[2]]

def custom_round(number, decimals=2):
    multiplier = 10 ** decimals
    return int(number * multiplier + 0.5) / multiplier

print(f"{custom_round(total_grade / total_unit, 2):.2f}")