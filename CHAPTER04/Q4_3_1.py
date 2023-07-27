def f(*args, separator="."):
    return separator.join(args)


print(f("3tyoume", "syurisueyosi", "nahasi", "okinawa", "japan", separator=" "))
