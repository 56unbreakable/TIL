CroatiaAlpahbet = ["c=","c-","dz=","d-",'lj','nj','s=','z=']

word = input()
sum=0
for i in CroatiaAlpahbet:
    while(word.find(i)!= -1):
        idx = word.find(i)
        word =word[:idx] +","+ word[idx+len(i):]
print(len(word))