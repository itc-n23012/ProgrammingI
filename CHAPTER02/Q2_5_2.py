a = ""
for i in range(4):
    for j in range(4):
        a += "● " if i != j else "○ "
    a += "\n"

print(a)
