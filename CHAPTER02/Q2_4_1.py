a = ""
b = 23
while b != 0:
    b, c = divmod(b, 2)
    a += str(c)

print(a[::-1])
