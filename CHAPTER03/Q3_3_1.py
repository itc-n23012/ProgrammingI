my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
a = []
for i in my_list:
    if len(i) >= 6:
        a.append(i)
print(a)
