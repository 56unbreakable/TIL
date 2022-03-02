""" string = input()

for i in range(len(string)):
    if string[i] == string[-(i+1)]:
        pal = 1
    else :
        pal = 0
        break

print(pal) """

# 슬라이싱으로 풀기

string = input()
if(string[-1:-(int(len(string)/2)+1):-1] == string[0:int(len(string)/2)]):
    pal = 1
else:
    pal = 0

print(pal)
