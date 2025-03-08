import cv2

video = cv2.VideoCapture("./data/video.mp4")
fourcc = cv2.VideoWriter.fourcc(*'FMP4')
writeVideo = cv2.VideoWriter('./data/writeVideo.mp4',fourcc,24,(1080,720))

while(video.isOpened()):
    suc, frame = video.read()
    if(suc):
        frame = cv2.resize(frame,(1080,720))
        cv2.imshow("write video",frame)
        writeVideo.write(frame)
        if(cv2.waitKey(24)&0xFF == ord('q')):
            break
    else:
        break

writeVideo.release()
video.release()
cv2.destroyAllWindows()