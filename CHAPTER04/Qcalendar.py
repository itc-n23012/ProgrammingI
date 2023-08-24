def colored_calendar(year, month):
    days = ["  " if (day == 0) else f"{day:2}" for day in range(1, 32)]
    weekdays = "月 火 水 木 金 土 日"
    days.insert(0, "  ")

    header = f"{year}年{month}月"
    print(header.center(21))
    print(weekdays)

    for i in range(0, len(days), 7):
        week = days[i : i + 7]
        week_str = [
            f"\033[34m{day}\033[0m"
            if idx == 5
            else f"\033[31m{day}\033[0m"
            if idx == 6
            else day
            for idx, day in enumerate(week)
        ]
        print(" ".join(map(str, week_str)))


if __name__ == "__main__":
    year = 2023
    month = 8
    colored_calendar(year, month)
