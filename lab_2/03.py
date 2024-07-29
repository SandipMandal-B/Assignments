import math

a, b, c = 1, -7, 10
d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are:", root1, "and", root2)
elif d == 0:
    root = -b / (2*a)
    print("Root is:", root)
else:
    print("No real roots")
