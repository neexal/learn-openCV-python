import cv2

img = cv2.imread('assets/img1.jpg')

imgCropped = img[0:300, 0:300] #height,width [start:end of height, start:end of width]


cv2.imshow('Original', img)
cv2.imshow("cropped image", imgCropped)

cv2.waitKey(0)