def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

result = power(3, 4)
print("3 to the power of 4:", result)
