import cv2

image = cv2.imread("./data/openCV_logo.jpg",cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(600,600))
cv2.imwrite("./data/openCV_logo_grayscale.jpg",image)

cv2.destroyAllWindows()