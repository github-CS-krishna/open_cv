from time import time
import cv2
previousTime = currentTime = fps = 0
video = cv2.VideoCapture("./data/video.mp4")
while(video.isOpened()):
    currentTime = time()
    ret,frame = video.read()

    if(not(ret)):
        break
    
    fps = 1/(currentTime-previousTime)
    previousTime = currentTime
    fps = "FPS "+str(int(fps))

    image = cv2.resize(frame,(800,600))
    cv2.putText(image,fps,(35,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,130),2,cv2.LINE_AA)
    cv2.imshow("show video FPS",image)
    
    if(cv2.waitKey(10)&0xff == ord('q')):
        break

cv2.destroyAllWindows()