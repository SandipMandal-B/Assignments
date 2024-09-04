def is_divisible_by_5(number):
    return number % 5 == 0

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by 5
if is_divisible_by_5(number):
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")
