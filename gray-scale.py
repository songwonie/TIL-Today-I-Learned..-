import cv2
import matplotlib.pyplot as plt

# gray-scale image
img = cv2.imread('cxap.png', cv2.IMREAD_GRAYSCALE) 
# 위와 같이 cv2.IMREAD_GRAYSCALE 와 같은 flag는 docs.opencv.org/master/
# 주소로 보면 좋다.

cv2.imshow('image', img)

# matplotlib 로 출력시에는 cmap= flag를 이용!
plt.imshow(img, cmap='gray')

while True:
    if cv2.waitKey() == 27: # esc키 종료 버튼
        break

