import cv2

img = cv2.imread('assets/img.jpg')
print(img.shape) #(height,width,channel)

imgResize = cv2.resize(img,(300,200)) #width,height
print(imgResize.shape)

cv2.imshow('Original', img)
cv2.imshow("resized image", imgResize)

cv2.waitKey(0)