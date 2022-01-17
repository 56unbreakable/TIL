'''
class grade_management :  # 클래스 선언
    def student_sum(self,st): # 학생의 점수 총합
        self.key = []  # 딕셔너리의 키를 받을 리스트
        self.value = [] # 딕셔너리의 밸류를 받을 리스트
        self.st_sum = 0 # 학생의 점수 총합
        for k,v in st.items(): # 키와 밸류를 리스트에 저장
            self.key.append(k)
            self.value.append(v)
        self.value = self.value[1:len(self.value)] # 밸류의 첫 값은 이름이기 때문에 점수가 들어가는 두번째 값부터 저장
        for i in range(len(self.value)): # 점수의 총 합을 저장
            self.st_sum += self.value[i]
        return self.st_sum # 점수의 총 합을 리턴.
    
    def student_avg(self,st):
        self.st_avg = 0
        self.st_avg = self.student_sum(st) / (len(st) - 1)  # 딕셔너리의 길이에서 이름을 뺀 값으로 총합을 나눔
        return self.st_avg
    
    def print_grade(self,st): # 학생 성적 출력
        a = '%s %2s %6s  %6s %6d   %6.2f'%(st['이름'],st['국어'],st['영어'],st['수학'],self.student_sum(st),self.student_avg(st))
        return a
    
    def subject_sum(self,st): # 각 과목의 총점 출력
        self.key = []     # 딕셔너리의 키를 받을 리스트
        self.value = []   # 딕셔너리의 밸류를 받을 리스트
        self.sum = []     # 점수의 총합을 받을 리스트
        for i in st:      # 받은 인자의 수 만큼 반복
            for k,v in i.items():  # 딕셔너리의 키와 밸류 나눔
                self.key.append(k)  
                self.value.append(v)
            self.value = self.value[1:len(self.value)]  # 첫번째인자는 이름이기때문에 제거
            for i in range(len(self.value)):  # 밸류의 길이만큼 반복
                if len(self.sum) < len(self.value) :  # sum의 길이가 value보다 짧으면
                    self.sum.append(0) # sum의 공간을 확보
                else : # 아니면 패스
                    pass
                self.sum[i] += self.value[i]  # 과목별 점수 합
            self.key = []   # 다음 인자의 딕셔너리를 받기 위해 키와 밸류를 담는 리스트를 초기화
            self.value = []
        return(self.sum)    # 점수의 총합을 리턴
    

mag = grade_management()  # 클래스 선언

#학생정보입력
st1 = {'이름' : '홍길동' , '국어' : 90, '영어' : 88, '수학' : 55}
st2 = {'이름' : '김기영' , '국어' : 77, '영어' : 66, '수학' : 100}
st3 = {'이름' : '곽진수' , '국어' : 88, '영어' : 99, '수학' : 98}
st4 = {'이름' : '김진수' , '국어' : 68, '영어' : 49, '수학' : 78}
st5 = {'이름' : '진영만' , '국어' : 98, '영어' : 90, '수학' : 92}
st6 = {'이름' : '신홍일' , '국어' : 38, '영어' : 85, '수학' : 94}

# 학생 리스트. 학생정보입력에 학생 딕셔너리를 추가하고 해당 객체를 학생 리스트에 추가하면된다.
st_list = [st1,st2,st3,st4,st5,st6]

all_student = len(st_list)
a = mag.subject_sum(st_list)

f = open('성적관리_list.txt','w')
f.write('{}   {}   {}   {}   {}   {}'.format('이름','국어','영어','수학','총점','평균'))
f.write('\n----------------------------------------\n')
for i in (st_list):
    f.write(mag.print_grade(i))
    f.write('\n')
f.write('----------------------------------------\n')
f.write('총점  %d  %6d %6d %6d   %6.2f'%(a[0],a[1],a[2],sum(a),sum(a)/all_student))
f.write('\n')
f.write('평균  %.2f  %6.2f %6.2f  %6.2f %1.2f'%(a[0]/all_student,a[1]/all_student,a[2]/all_student,sum(a)/all_student,(sum(a)/all_student)/3))
f.close
'''
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