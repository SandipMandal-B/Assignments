def count_letters_and_digits(input_string):
    letters_count = 0
    digits_count = 0

    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1

    return letters_count, digits_count


input_string = "hello world! 123"
letters, digits = count_letters_and_digits(input_string)
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
