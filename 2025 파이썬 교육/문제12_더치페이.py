cost = int(input("발생한 총 비용을 입력하세요. : "))
bye = int(input("헤어진 시간을 입력하세요. (예: 2400) : "))
if not (1 <= bye <= 2400):
    print("다시 입력하세요.")
    exit()

name = list(map(str, input("참석자의 이름을 모두 입력하세요 : ").split()))
hello_times = {}

for person in name:
    time = int(input(f"{person}님의 참석 시간을 입력하세요. (예: 1230) : "))
    if not (1 <= time <= 2400):
        print("다시 입력하세요.")
        exit()
    hello_times[person] = time

h2, m2 = divmod(bye, 100)
bye_minutes = h2 * 60 + m2

total_all_minutes = 0
person_minutes = {}

for person, h_time in hello_times.items():
    h1, m1 = divmod(h_time, 100)
    person_total = bye_minutes - (h1 * 60 + m1)
    person_minutes[person] = person_total
    total_all_minutes += person_total

if total_all_minutes <= 0:
    print("계산할 수 없습니다.")
else:
    for person in name:
        share = round(cost * person_minutes[person] / total_all_minutes)
        print(f"{person}님 {share:,}원")
