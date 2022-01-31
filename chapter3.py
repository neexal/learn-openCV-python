import cv2
import numpy as np

img = cv2.imread('assets/img1.jpg')
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
imgBlur = cv2.GaussianBlur(img,(7,7),0) #img, ksize(should be odd, sigmaX=0)

imgCanny = cv2.Canny(img,150,200) #for edge detection
imgDialation = cv2.dilate(imgCanny,kernel, iterations=5) #for marking edge detection better, making edge thicker
imgEroded = cv2.erode(imgGray,kernel,iterations=1) #for marking edges thinner

cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Edge Detection', imgCanny)
cv2.imshow('Image Dilation', imgDialation)
cv2.imshow('Image Erosion', imgEroded)
cv2.waitKey(0)