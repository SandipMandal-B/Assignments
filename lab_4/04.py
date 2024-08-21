input_string = "hello world and practice makes perfect and hello world again"
words = input_string.split()
unique_words = set(words)
sorted_words = sorted(unique_words)
output_string = ' '.join(sorted_words)
print(output_string)