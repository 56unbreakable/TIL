print("frist array")
arr1 = [list(map(int, input().split())) for i in range(2)]
print("second array")
arr2 = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(arr1[i][j]*arr2[i][j], end=" ")
    print()
