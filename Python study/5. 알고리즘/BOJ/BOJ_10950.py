testcaseNum = int(input())

repNum = 0
aarr = []
barr = []
while(repNum < testcaseNum):
    a, b = map(int, input().split())
    aarr.append(a)
    barr.append(b)
    repNum += 1

for i in range(testcaseNum):
    print(aarr[i]+barr[i])
