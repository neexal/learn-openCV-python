import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# img[0:200,0:300]=[255,0,0] #BGR height,width coloring image

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3) #img,startpoints, endpoints,color,thickness

cv2.rectangle(img,(0,0),(150,200),(255,0,0),1) #img,startpoints, endpoints,color,thickness(use cv2.FILLED for filled rectangle))))
cv2.circle(img,(256,256),30,(0,0,255),1) #img,center,radius,color,thickness
cv2.putText(img,"Hello World",(100,100),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,255,255),2) #img,text,startpoints,font,fontsize,color,thickness
cv2.imshow("Image", img) 



cv2.waitKey(0)