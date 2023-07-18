import random

a = [i for i in range(10)]
n = random.sample(a, k=4)
ans = []

while True:
    while True:
        b = input("4桁の数字を入れてください  ")
        if len(b) == 4:
            if b[0] != b[1] != b[2] != b[3]:
                break
            else:
                print("異なる数字を入れてください")
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
        print("正解")
        break
