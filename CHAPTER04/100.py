num = [str(i + 1) for i in range(100)]
print("\n".join(" ".join(num[i :  i + 10]) for i in range(0, 100, 10)))
