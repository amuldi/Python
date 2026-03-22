x,y,w,h = map(int, input().split())

left_x = x
left_y = y
right_w = w - x
right_h = h - y

min_value = min(left_x, left_y, right_w, right_h)
print(min_value)
