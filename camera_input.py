import sys
import cv2

# opencv의 VideoCapture 클래스
# VideoCapture 클래스는 filename이 들어가면 특정 파일명의 동영상 open
# 반대로, filename이 아닌, 숫자(정수) 형태로 들어가면, 인덱스로 지정된 특정 카메라의 영상을 받아옴

cap = cv2.VideoCapture(0) # 0번 카메라에서 받아오겠다.
#print(cap.shape)

if not cap.isOpened():
    print("camera open Failed!")
    sys.exit()

# 무한루프 안에서 한 프레임씩 카메라를 가져옴
while True:
    ret, frame = cap.read() # ret(return)가 반환안하면 False로,
                            # ret가 반환하면 True로, 
                            # frame은 반환안하면 None으로 들어감
    if not ret: # ret가 True가 아니면,
        break

    if frame is None: # 이렇게도 들어감
        break

    # 캐니-엣지 노이즈 추가
    edge = cv2.Canny(frame, 50, 150) # frame은 한장의 정지 영상이라서, 

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(1) == 27:
        break

cap.release() # 안써도 된다.