# Q1.
# shirt

# Q2
a=0
sum=0
while a<1000:
    a += 1 
    if a%3 == 0:
        sum+=a
    else:
        continue
print(sum)

# Q3
a = 1
k = '*'
while a < 6:
    j = k*a
    print(j)
    a+=1

# Q4
for i in range(1,101):
    print(i)

# Q5
a = [70,60,55,75,95,90,80,80,85,100]
sum = 0
for i in a:
    sum += i
print(sum/len(a))

# Q6
n = [1,2,3,4,5]
result = [n*2 for n in n if n % 2 == 1]
print(result)