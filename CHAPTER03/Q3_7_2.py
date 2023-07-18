with open("number.txt", "r") as f:
    sum = 0
    for date in f:
        num = int(date)
        sum += num
    print(sum)
