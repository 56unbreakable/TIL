# 행이 맞는지 확인
# 열이 맞는지 확인
# 3*3이 맞는지 확인

row_check = False
col_check = False
square_check = False
sudoku = []

testcase_num = int(input())
for t in range(testcase_num):
    for i in range(9):
        s_row = list(map(int,input().split()))
        sudoku.append(s_row)
        for j in range(9):
            if j in s_row:
                row_check = True
            else:
                row_check = False
    
    if row_check == False:
        break

    for i in range(9):
        for j in range(9):
            if sudoku[j][i]