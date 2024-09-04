
def is_perfect_number(num):
    return num == sum(i for i in range(1, num) if num % i == 0)


def is_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    return num == sum(d ** len(digits) for d in digits)


num = 153

if is_perfect_number(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
