word = input("enter a numebr or word: ")

rev = str(word)[::-1]

if rev == word:
    print(f"{word} is palindrome")