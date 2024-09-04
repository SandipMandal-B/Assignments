str = input("enter a string with comma: ")

words = str.split(',')

words.sort()

sorted_string = ','.join(words)

print(sorted_string)