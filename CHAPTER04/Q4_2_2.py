def f(m):
    a, b, c = 3, 0, 2
    result = []
    while a < m:
        result.append(a)
        a, b, c = b, c, a + b
    print(result)


f(100)
