testcaseNum = int(input())

for i in range(testcaseNum):
    misspell, misstr = input().split()
    misspell = int(misspell)
    k = misstr[0:misspell-1] + misstr[misspell:]
    print(k)