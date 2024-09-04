def display_numbers():
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            print(num)

display_numbers()
