def f(num=0):
    n = num % 7
    return (
        "水曜日"
        if n == 0
        else "木曜日"
        if n == 1
        else "金曜日"
        if n == 2
        else "土曜日"
        if n == 3
        else "日曜日"
        if n == 4
        else "月曜日"
        if n == 5
        else "火曜日"
    )


num = int(input())
print(f(num))
