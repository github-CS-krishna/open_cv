import cv2

video = cv2.VideoCapture('./sample_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('./output.avi',fourcc,25,(256,144))
while(video.isOpened()):
    suc, frame = video.read()
    if(suc):
        frame = cv2.resize(frame,(1280,720))
        out.write(frame)
        cv2.imshow("camera",frame)
        if(cv2.waitKey(25) == ord('q')):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()