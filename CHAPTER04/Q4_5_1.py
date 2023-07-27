function = [sum, min, max]
number_list = range(1, 11)
for func in function:
    print("unction: {}, Result: {}".format(func.__name__, func(number_list)))
