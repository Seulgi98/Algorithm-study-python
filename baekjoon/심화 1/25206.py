grade_points = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

total_subject = 0.0
total_credits = 0.0

for _ in range(20):
    input_list = input().split()
    subject = input_list[0]
    credit = float(input_list[1])
    grade = input_list[2]

    if grade == 'P':
        continue

    total_credits += credit
    total_subject += credit * grade_points[grade]

grade_average = total_subject / total_credits
print(f"{grade_average:.6f}")
