
raw_word = input("GIVE WORD: ")
word = ''
i = 1
for letter in range(len(word)):
    if (i % 2)==0:
        word = word + raw_word[letter].lower()
    elif (i % 2)!=0:
        word = word + raw_word[letter].upper()
    i = i + 1

print(word)