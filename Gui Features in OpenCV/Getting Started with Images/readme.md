# Getting Started with Images

## 🎉 a.py

```py
# import modules : 모듈 불러오기
import cv2 as cv
import sys

# 사진 가져오기(읽기)
img = cv.imread(cv.samples.findFile("./Gui Features in OpenCV/Getting Started with Images/starry_night.jpg"))

# 이미지를 불러오는데 실패(None)했을 때, 나가기
if img is None:
    sys.exit("Could not read the image.")

# 이미지 쇼
cv.imshow("Display window", img)

# 키보드 입력 대기
k = cv.waitKey(0)

# 입력한 키가 s라면 저장
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
```

### ✨ cv.imread([FILE])

FILE 주소를 입력 받아서 그 주소의 사진을 읽어오는 함수

---

### ✨ cv.imwrite([FILE])

