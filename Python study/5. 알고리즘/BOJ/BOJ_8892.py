testcaseNum = int(input())

for i in range(testcaseNum):
    arr = []
    pal = 0
    wordNum = int(input())
    for j in range(wordNum):
        word = input()
        arr.append(word)

    for j in range(len(arr)):
        for k in range(1, len(arr)-j):
            string = arr[j] + arr[j+k]
            if(string[-1:-(int(len(string)/2)+1):-1] == string[0:int(len(string)/2)]):
                pal = string

    for j in range(len(arr)):
        for k in range(1, len(arr)-j):
            string = arr[j+k] + arr[j]
            if(string[-1:-(int(len(string)/2)+1):-1] == string[0:int(len(string)/2)]):
                pal = string
    print(pal)
