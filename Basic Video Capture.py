import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,100)


while True:
    success ,img = cap.read()
    cv2.imshow("Video",img)
    key = cv2.waitKey(1)
    if key == ord(' '):
        break
cap.release()
# to release the video that we have created i.e the images that we have been capturing through our web_cam
cv2.destroyAllWindows        
#to destroy all the win
