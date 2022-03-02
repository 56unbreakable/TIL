testcaseNum = int(input())

for i in range(testcaseNum):
    num, s = input().split()
    for j in s:
        for k in range(int(num)):
            print(j,end="")
    print()