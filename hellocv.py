import sys
import cv2

print("opencv-versions: ", cv2.__version__) # opencv 버전 확인

img = cv2.imread('cxap.png') # img는 ndarray 다차원 형태 배열로 불러옴

if img is None: # 이미지 파일 불러올때,못불러온 경우를 항상 예외처리 해두는게 좋다!
    print("Image Load Failed!")
    sys.exit()

print(type(img)) 
print(img.shape) #영상의 크기,정보,차원을 확인가능
print(img.dtype) #영상의 데이터 타입 확인가능

cv2.namedWindow('image_show')
cv2.imshow('image_show', img) # imga_show라는 창에 이미지를 보여줘
cv2.waitKey() # 키입력 기다리는 인자, '0'을 입력하면 무한대로 기다림
cv2.destroyAllWindows() # 보통은 생략을 해도됨, 다만 function이 끝나고 종료하라는 의미로



