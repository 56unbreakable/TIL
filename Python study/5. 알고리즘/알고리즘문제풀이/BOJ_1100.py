chess = [list(input()) for i in range(8)]

# (0,0)이 흰칸, (1,1)이 흰칸 (2,0)이 흰칸. 즉 둘다 짝수거나 둘다 홀수여야 흰칸
white = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == "F":
            white += 1
        elif i % 2 == 1 and j % 2 == 1 and chess[i][j] == "F":
            white += 1
print(white)
