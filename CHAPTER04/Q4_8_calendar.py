import calendar


def f(year=2023, month=8):
    cal = calendar.TextCalendar()
    cal.setfirstweekday(calendar.SUNDAY)
    weekdays = "日 月 火 水 木 金 土"
    print(weekdays)

    for week in cal.monthdayscalendar(year, month):
        week_str = [
            f"\033[31m  \033[0m"
            if day == 0
            else f"\033[31m{day:2}\033[0m"
            if day % 7 == 6
            else f"\033[34m{day:2}\033[0m"
            if day % 7 == 5
            else f"{day:2}"
            for day in week
        ]
        print(" ".join(week_str))


f()
