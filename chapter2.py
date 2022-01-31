import cv2
from outcome import capture

# video or webcam capture in opencv
# capture=cv2.VideoCapture('assets/video.mp4') #for displating video
capture = cv2.VideoCapture(0) #for displating webcam
capture.set(3, 640) #for width
capture.set(4, 480)  #for height
capture.set(10, 100)  #for brightness

while True:
    success, img = capture.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break