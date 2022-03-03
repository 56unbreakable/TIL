testcaseum = int(input())

rep_num = 0
aarr = []
barr = []
while(rep_num < testcaseum):
    a, b = map(int, input().split())
    aarr.append(a)
    barr.append(b)
    rep_num += 1

for i in range(testcaseum):
    print(aarr[i]+barr[i])
