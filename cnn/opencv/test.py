import cv2
import matplotlib.pyplot as plt
import sys

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)  # 사진 파일 가져오기

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #그래프로 출력
plt.show()

if img is None:
    print("Image Load Failed")
    sys.exit() # 시스템 종류

cv2.imwrite('cat_gray.png',img)
cv2.imshow('image',img)
cv2.waitKey()

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows()