score = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

average = 0.0
totall = 0.0

for i in range(20):
    lecture, credit, grade = input().split()
    if grade == 'P':  
        continue
    else:
        average += float(credit) * score[grade]
        totall += float(credit)

if totall == 0:
    print("0.000000")
else:
    print(f"{average / totall:.6f}")