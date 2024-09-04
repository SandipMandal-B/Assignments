def check_yes(input_string):
    if input_string in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")


input_string = input("Enter a string: ")
check_yes(input_string)
