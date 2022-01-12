import turtle as t

# 사각형 그리기
line = t.Turtle()

# 50만큼 앞으로 이동
line.forward(50)

# 오른쪽으로 90도 꺾음. left일경우 왼쪽으로 회전
line.right(90)
line.forward(50)
line.right(90)
line.forward(50)
line.right(90)
line.forward(50)

print("7+4 = ", 7+4)

# 제곱 표시 2**3 = 2*2*2
print("2**4 = ", 2**4)

# 반복문
for x in range(10):
    print("Hello!")
# range(1, 10) -> 1부터 10까지 1간격으로.

# 반목문을 사용한 삼각형, 사각형 그리기.
tri = t.Turtle()
for x in range(3):
    tri.forward(100)
    tri.right(120)

rec = t.Turtle()
for x in range(4):
    rec.forward(100)
    rec.right(90)

print("[0-4]")
for x in range(4):
    print(x)

# 반복문 예제
sum = 1
for x in range(1,11):
    sum *= x
    print("x : ", x, " sum ", sum)

# 반복문을 이용한 도형 그리기
n = 5
t.color("blue")
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()

n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

# 정보 입력 
name = input("your name? ")
# your name? 을 출력하고 입력을 받는다. 입력을 받고 엔터를 누르면
# name에 입력값을 저장한다.
print("Hello", name)

# input으로 입력된 변수는 str형으로 저장됨.
# int(x)로 정수형으로 변환시켜줘야 연산 가능
x = input()
a = int(x)
x = input()
b = int(x)
print(a*b)

# 추가 : type(x)로 x의 자료형을 확인할 수 있음.

# if문
a=3
if a==2:
    print("a")    
if a==3:
    print("b") 
if a==4:
    print("c")
else:
    print("d")

# if문 예제
x = input("12+23 = ?")
a = int(x)
if a == 12+23:
    print("천재")
else:
    print("바보")

# while문
x = 1
sum=1
while x<=10:
    print(sum)
    x = x+1
    sum += x

'''
** 함수의 기본 구조 **
def 함수이름 (인자) :   -> 인자는 필요없으면 생략 가능
    함수 내용
    return c    -> c를 결과값으로 가져옴
'''

# 함수
def hello():
    print("hello")
hello()

def hello2(name):
    print("hello",name)
hello2("seunghwan")

def square(a):
    c = a*a
    return c

def triangle(a,h):
    c = a*h /2
    return c

s1 = 4
s2 = square(s1)
print(s1,s2)

print(triangle(3,4))

def sum_func(n):
    s=0
    for x in range(1,n+1):
        s += x
    return s

print(sum_func(10))

