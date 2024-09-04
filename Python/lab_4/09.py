def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def ends_with(s, substring):
    return s.endswith(substring)

def capitalize_each_word(s):
    return s.title()

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

def longest_word_length(s):
    words = s.split()
    return max(len(word) for word in words)


input_string = input("Enter a string: ")
substring = input("Enter a substring to check if the string ends with it: ")

print(f"Reversed string: {reverse_string(input_string)}")
print(f"Is palindrome: {is_palindrome(input_string)}")
print(f"Ends with '{substring}': {ends_with(input_string, substring)}")
print(f"Capitalized: {capitalize_each_word(input_string)}")


str1 = input("Enter the first string to check anagram: ")
str2 = input("Enter the second string to check anagram: ")
print(f"Are anagrams: {are_anagrams(str1, str2)}")

print(f"String without vowels: {remove_vowels(input_string)}")
print(f"Length of the longest word: {longest_word_length(input_string)}")
