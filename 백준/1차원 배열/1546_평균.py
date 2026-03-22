N = int(input())
scores = list(map(int,input().split()))
maxscore = max(scores)

jojak = [score / maxscore * 100 for score in scores] #리스트 컴프리헨션
average = sum(jojak)/N #평균 계산

print(average)