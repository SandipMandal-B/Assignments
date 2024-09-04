str = input("enter a string: ")
lenth = len(str)
print("length of the string is : ",lenth)

if 'country' in str:
    print("country forund")
else:
    print("country not found int he string")


word_count = {}
words = str.split()

for word in words:
    word = word.strip('.').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")