print("frist array")
arr1 = [list(map(int, input().split())) for i in range(2)]
print("second array")
arr2 = [list(map(int, input().split())) for i in range(2)]

arr3 = []

for i in range(2):
    temp_arr = []
    for j in range(4):
        temp_arr.append(arr1[i][j]*arr2[i][j])
    arr3.append(temp_arr)

for i in range(2):
    for j in range(4):
        print(arr3[i][j],end=" ")
    print()