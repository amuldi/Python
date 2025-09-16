def fibonacci(n, count):
    count += 1
    if n <= 1:
        contents = "if n<=1: Count: %d, current n: %d" % (count, n)
        print(contents)
        return 1
    else:
        contents = "else: Count: %d, current n: %d" % (count, n)
        print(contents)
        return fibonacci(n-1, count) + fibonacci(n-2, count)

fibonacci(6, count=1)

#재귀 호출 순서 변경
"""def fibonacci(n, count):
    count += 1
    if n <= 1:
        contents = "if n<=1: Count: %d, current n: %d" % (count, n)
        print(contents)
        return 1
    else:
        contents = "else: Count: %d, current n: %d" % (count, n)
        print(contents)
        return fibonacci(n-2, count) + fibonacci(n-1, count)

fibonacci(6, count=1)"""