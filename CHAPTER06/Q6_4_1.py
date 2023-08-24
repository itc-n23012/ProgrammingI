with open("some.txt") as f:
    for c, l in enumerate(f):
        if c == 2:
            break
        print(l, end="")
