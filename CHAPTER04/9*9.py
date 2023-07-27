def f(n):
    for i in range(1, n + 1):
        for a in range(1, n + 1):
            print(f"{i * a: {len(str(n*n))+1}d}", end="")
        print(end="\n")


n = int(input())
f(n)
