# 명함 검출/인식 proj.
import sys
import cv2

src = cv2.imread('namecard1.jpg')
if src is None:
    print('Image Load Failed!')
    sys.exit()

# opencv, 영상의크기를 줄여줌 resize()
# src = cv2.resize(src, (640, 480)) resize 하려는 특정 사이즈를 입력할 수 있음
# x, y방향으로 반으로 줄이겠다. 아래와 같이 가능! 
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5) 
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 이진환 func: Treshold() 3강 24:31

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.waitKey()