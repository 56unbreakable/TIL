# day 28

## opneCV

### openCV-python

`pip install opencv-python` 으로 아나콘다에서 설치

#### 영상 파일 불러와서 출력

`cat.bmp` 파일을 불러와서 출력할 수 있다.

```python
import cv2
import matplotlib.pyplot as plt
import sys

img = cv2.imread('cat.bmp')  # 사진 파일 가져오기

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #그래프로 출력
plt.show()

if img is None: # 만약 사진을 불러오지 않을경우
    print("Image Load Failed")
    sys.exit() # 시스템 종류

# 이미지 창을  띄우고 키보드를 누를 경우 창 종료
cv2.namedWindow("image")
cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows()
```

특정 키를 누르면 창이 종료되게 할 수 있다.

```python
cv2.imwrite('cat_gray.png',img)
cv2.imshow('image',img)
cv2.waitKey()

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows()
```

`q` 를 누르면 창이 종료된다.

#### matplotlib

두 개의 영상을 함께 출력

```python
import cv2
import matplotlib.pyplot as plt

# 컬러영상출력
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray,cmap='gray')
plt.show

# 두 개의 영상을 함께 출력
plt.subplot(121),plt.axis('off'),plt.imshow(imgRGB)
plt.subplot(122),plt.axis('off'),plt.imshow(imgGray,cmap='gray')
plt.show
```

#### 이미지 슬라이드쇼

여러개의 이미지를 연속으로 슬라이드쇼로 만들 수 있다.

```python
import sys
import glob
import cv2

# `img_files` 리스트에 `images` 폴더에 있는 `jpg` 파일을 모두 저장
img_files = glob.glob('.\\images\\*.jpg')

# 이미지 폴더가 존재하지 않을 경우 메세지 출력 후 시스템종료
if not img_files:
    print("There are no jpg files im 'images' folder")
    sys.exit()

# 전체화면으로 `image` 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한루프로 이미지 슬라이드쇼. `waitKey` 로 키를 누를 시 종료
cnt = len(img_files)
idx = 0

while True:
    img=cv2.imread(img_files[idx])

    if img is None:
        print("image load failed")
        break

    cv2.imshow('image',img)
    if cv2.waitKey(1000)>=0:
        break

    idx+=1
    if idx>=cnt:
        idx=0

cv2.destroyAllWindows()
```

#### 영상의 속성

영상의 속성을 확인해볼 수 있다.

```python
import sys
import cv2

img1 = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp',cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('image load failed')
    sys.exid()

# 영상의 속성 참조
print('type(img1) : ',type(img1))
print('img1.shape : ',img1.shape)
print('img2.shape : ',img2.shape)
print('img1.dtype : ',img1.dtype)

h,w = img2.shape[:2]
print("img2 size : {} x {}".format(w,h))

if len(img1.shape) == 2:
    print('img1 is grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
for y in range(h):
    for x in range(w):
        img1[y,x] = 255
        img2[y,x] == (0,0,255)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.waitKey()

cv2.destroyAllWindows()
```

#### 영상변경 : 픽셀처리

```python
import numpy as np
import cv2

img1 = np.empty((240,320),dtype=np.uint8)
img2 = np.zeros((240,320,3),dtype=np.uint8)
img3 = np.ones((240,320),dtype=np.uint8) * 255
img4 = np.full((240,320,3),(0,255,255),dtype=np.uint8)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)

cv2.waitKey()

cv2.destroyAllWindows()
```

#### 영상변경 : 복사, 추출

다음 코드를 사용하면 같은 이미지가 3개가 출력된다.

```python
import cv2

img1 = cv2.imread('HappyFish.jpg')

img2 = img1
img3 = img1.copy()

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()
```

다음 코드를 사용하면 이미지 세개가 다르개 출력된다.

```python
import cv2

img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]
img3 = img1[40:120,30:150].copy()

img2.fill(0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()
```

`img2` 는 `fill(0)` 을 했기 때문에 검정화면이 출력된다.

`img3` 는 `img1` 에서 추출하였고, `img1` 은 추출된 만큼 0처리된다. 즉, `img1` 에서 추출한 `img3` 만큼 없어지고, `img3` 는 `img1` 에서 추출한 만큼 보인다.

#### 영상변경 : 마스크연산

```python
import sys
import cv2

src = cv2.imread('airplane.bmp',cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp',cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print("image load failed")
    sys.exit()

cv2.copyTo(src, mask, dst)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('mask',mask)
cv2.waitKey()
cv2.destroyAllWindows()
```

`field.bmp` 와 `airplane.bmp` 을 합친 영상을 만들 수 있다.

`src` 에 `airplane.bmp` 를 저장, `mask` 에 `mask_plane.bmp` 저장한다. `mask_plane.bmp` 는 특정 위치를 따오기 위한 파일이다. 이 예제에서는 비행기의 모양을 따오기 위한 파일이다.

`dst` 에는 배경이 될 사진을 저장한다.

`cv2.copyTO` 함수를 사용하여 `src` 를 `mask` 영역만큼 따와 `dst` 에 저장한다. 최종 결과물은 `dst` 에 출력되는데, `airplane.bmp` 에서 `mask_plane.bmp` 에 따와져있는 영역만큼 이미지를 따서 `field.bmp` 에 카피한다.

#### 영상변경 : 동영상 이펙트

```python
import sys
import numpy as np
import cv2

cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print("video open failed")
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps*2)

print("frame_cnt1",frame_cnt1)
print("frame_cnt2",frame_cnt2)
print("fps : ",fps)

delay = int(1000/fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi',fourcc,fps,(w,h))

for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print("frame read erroer")
        sys.exit()

    out.write(frame1)
    print('.',end="")

    cv2.imshow('output', frame1)
    cv2.waitKey(delay)
```

