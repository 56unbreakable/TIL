class Cstuendt:
    def __init__(self,*st_info):
        self.count = len(st_info)
        self.sublist = []
        self.total = 0
        for i in range(0,self.count):
            self.sublist.append(st_info[i])

    def getName(self):
        return self.sublist[0]
    
    def getKor(self):
        return self.sublist[1]

    def getEng(self):
        return self.sublist[2]

    def getMath(self):
        return self.sublist[3]

    def getTotal(self):
        self.total = 0
        for i in range(1,self.count):
            self.total += self.sublist[i]
        return self.total

    def getAvg(self):
        return self.total/(self.count-1)

stuList = []
stuList.append(Cstuendt('홍길동',90,88,55))
stuList.append(Cstuendt('김기영',77,66,100))
stuList.append(Cstuendt('곽진수',88,99,98))

totalSum = 0
subSum = [0,0,0]

for i in range(len(stuList)):
    totalSum += stuList[i].getTotal()

for i in range(len(stuList)):
    subSum[0] += stuList[i].getKor()
    subSum[1] += stuList[i].getEng()
    subSum[2] += stuList[i].getMath()

f = open('성적관리_list.txt','w')
f.write('이름   국어   영어   수학   총점   평균')
f.write('\n')
for i in stuList:
    f.write('%s  %d  %6d %6d %6d   %6.2f'%(i.getName(),i.getKor(),i.getEng(),i.getMath(),i.getTotal(),i.getAvg()))
    f.write('\n')
f.write('총점   %d  %6d %6d %6d   %6.2f'%(subSum[0],subSum[1],subSum[2],totalSum,totalSum/len(stuList)))
f.write('\n')
f.write('총점   %d  %6d %6d %6d   %6.2f'%(subSum[0]/3,subSum[1]/3,subSum[2]/3,totalSum/len(stuList),totalSum/len(stuList)/3))
f.close