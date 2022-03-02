word = input()

censoredWord = "CAMBRIDGE"
for i in censoredWord:
    while(word.find(i) != -1):
        idx = word.index(i)
        word = word[:idx] + word[idx+1:]
print(word)