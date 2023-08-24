import my_math

with open("my_math.py", "w") as f:
    f.write(
        """def my_pow(x, y):
            return x ** y\n"""
    )


print(my_math.my_pow(2, 5))
