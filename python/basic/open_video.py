import cv2

video = cv2.VideoCapture("./data/video.mp4")

while(video.isOpened()):
    isTrue, frame = video.read()
    if(isTrue):
        frame = cv2.resize(frame,(800,500))
        cv2.imshow("play video",frame)
        if(cv2.waitKey(24)&0xFF == ord('q')):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()