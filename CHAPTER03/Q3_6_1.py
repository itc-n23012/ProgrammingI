import random

a = [i for i in range(10)]
n = random.sample(a, k=4)
n4 = "".join(str(n))
while True:
    b = int(input())
    if b == n4:
        print("ok")
        break
    else:
        print(b, ":NG")
