import cv2

def mouse_event(event,x,y,flag,params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.rectangle(img,(x,y),(x+150,y+150),(255,0,0),2)
        cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(200,0,0),2,cv2.LINE_AA)
        cv2.imshow("draw rectangle",img)

img = cv2.imread("./data/openCV_logo.jpg",cv2.IMREAD_COLOR)
cv2.imshow("draw rectangle",img)
cv2.setMouseCallback("draw rectangle",mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()