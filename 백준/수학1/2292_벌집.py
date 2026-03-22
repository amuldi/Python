n = int(input())
count = 1
max_num = 1
while max_num < n:
    max_num += 6 * count
    count += 1
print(count)

