wood = list(map(int, input().split()))

sort_incomplete = True

while(sort_incomplete):
    if wood[0] > wood[1]:
        wood[0], wood[1] = wood[1], wood[0]
        for i in range(5):
            print(wood[i], end=" ")
        print()
    if wood[1] > wood[2]:
        wood[1], wood[2] = wood[2], wood[1]
        for i in range(5):
            print(wood[i], end=" ")
        print()
    if wood[2] > wood[3]:
        wood[2], wood[3] = wood[3], wood[2]
        for i in range(5):
            print(wood[i], end=" ")
        print()
    if wood[3] > wood[4]:
        wood[3], wood[4] = wood[4], wood[3]
        for i in range(5):
            print(wood[i], end=" ")
        print()
    if sorted(wood) == wood:
        sort_incomplete = False
