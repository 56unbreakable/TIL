word = input()

censored_word = "CAMBRIDGE"
for i in censored_word:
    word = word.replace(i,"")
print(word)