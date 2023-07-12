import random

a = [chr(i) for i in range(97, 97 + 26)]

while True:
    initial = random.choices(a, k=2)
    print("・".join(initial))
    if initial == ["y", "k"]:
        break
