taebo = input()

idx = taebo.index("0")
taeboleft = taebo[:idx]
taeboright = taebo[idx:]

leftfist = taeboleft.count("@")
rightfist = taeboright.count("@")

print(leftfist, rightfist)
