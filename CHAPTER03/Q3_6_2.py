import random

a = [i for i in range(10)]
n = random.sample(a, k=4)
ans = []

while True:
    b = input()
    ok = 0
    osi = 0
    ans = [int(i) for i in b]
    for i in range(4):
        if ans[i] == n[i]:
            ok += 1
        elif ans[i] in n:
            osi += 1
        else:
            None
    print("○ " + str(ok) + "△ " + str(osi))
    if ok == 4:
        print("correct")
        break
