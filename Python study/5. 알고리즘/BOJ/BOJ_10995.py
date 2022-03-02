n = int(input())

for j in range(n):
    if(j % 2 == 1):
        for i in range(n):
            print(" *", end="")
    else:
        for i in range(n):
            print("* ", end="")
    print()
