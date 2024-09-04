#krishnamurthi nuber 

import math

def is_krishnamurthy(num):
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

num = 145

if is_krishnamurthy(num):
    print(num, "is a Krishnamurthy number")
else:
    print(num, "is not a Krishnamurthy number")
