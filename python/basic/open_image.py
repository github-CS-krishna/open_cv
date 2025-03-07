import cv2

image = cv2.imread("./data/openCV_logo.jpg",cv2.IMREAD_COLOR)
image = cv2.resize(image,(600,600))
cv2.imshow("window title",image)

cv2.waitKey(0)

cv2.destroyAllWindows()