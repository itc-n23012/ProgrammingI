def f(*args):
    result = []
    for i in args:
        result.append(i * i)
    return result


numbers = list(range(100))
print(f(*numbers))
