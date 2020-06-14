# Youtube 동영상 불러오기
# pafy 패키지와 youtube_dl 두개의 패키지 설치필요 : pip install 이용!
import pafy
import cv2

url = 'https://www.youtube.com/watch?v=amM3O0WX05w'
video = pafy.new(url)

# highest resolution, audio+video
best = video.getbest()
print(best, best.url)

cap = cv2.VideoCapture(best.url)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = round(1000/fps)

# 동영상 저장을 위한 cv2.VideoWriter 객체 생성
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 프레임의 너비
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 프레임의 높이
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #코덱정보 *'DIVX' == 'D','I','V','X'
out = cv2.VideoWriter('youtube_ouput_edge.avi', fourcc, fps, (w,h))

while True:
    ret, frame = cap.read()
    if not ret: break

    # 캐니-엣지 적용
    edge = cv2.Canny(frame, 50, 150)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # 유튜브 동영상을 저장!, 동영상을 한프레임씩 받아오면서 동시에 저장해나감
    out.write(edge)

    cv2.imshow('frame', frame)
    if cv2.waitKey(delay) == 27:
        break