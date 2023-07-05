grades = {'A+': 4.5, 'A0': 4.0,
          'B+': 3.5, 'B0': 3.0,
          'C+': 2.5, 'C0': 2.0,
          'D+': 1.5, 'D0': 1.0,
          'F': 0.0
          }

total, total_c = 0, 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade == 'P':
        continue
    total += float(credit) * grades[grade]
    total_c += float(credit)

# sum(학점 * 과목평점) / 학점 총합
print(total / total_c)
