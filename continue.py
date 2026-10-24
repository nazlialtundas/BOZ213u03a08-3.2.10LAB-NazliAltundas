word = input("Please enter a word: ").upper()
for letter in word:
    if letter in "AEIOU" :
        continue
    print(letter)
