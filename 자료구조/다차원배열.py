rows = 3      # 행(row)의 개수 = 3
cols = 3      # 열(column)의 개수 = 3

array_2d = [[i * cols + j for j in range(cols)] for i in range(rows)]

# [2][1] 위치의 원소 제거 (3행 2열, 값은 7)
# pop(1)은 인덱스 1 위치의 값을 꺼내면서 삭제
element_removed = array_2d[2].pop(1)

# 배열 출력 (삭제된 후 상태)
print("Updated 2D Array:")
for row in array_2d:   # 각 행(row)을 출력
    print(row)

# 삭제된 값 출력
print("Element removed:", element_removed)