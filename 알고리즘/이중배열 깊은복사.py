lab = [[1,2,3],[4,5,6]]

temp = [item[:] for item in lab]

temp[0][0] = 0
print(temp)
print(lab)