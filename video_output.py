# 동영상 파일로 저장 예제
import sys
import cv2

# 카메라로부터 cv2.VideoCapture 생성
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 동영상 저장을 위한 cv2.VideoWriter 객체 생성
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 프레임의 너비
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 프레임의 높이
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #코덱정보 *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('video_ouput.avi', fourcc, fps, (w,h))

# 매 프레임 처리 및 화면출력
while True:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 40, 150)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    # 비디오 파일 형식으로 저장!
    out.write(edge)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(1) == 27:
        break

# memory release
cap.release()
out.release()
cv2.destroyAllWindows()