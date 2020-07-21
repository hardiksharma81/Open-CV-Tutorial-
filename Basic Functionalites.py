import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)
#here ones means color and zero means black ! 
#here the matrix is of 5x5 and we have used unsinged int of 8 bit)

frame= cv2.imread("im 1.jpg")

gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#converting img into Gray Frame

blur = cv2.GaussianBlur(gray,(3,3),0)
#converting image into blur image

canny = cv2.Canny(frame,150,100)
#detecting the edgeds in the image
#the lower the values the fuzzier is the lines.

dilation = cv2.dilate(canny,kernal,iterations = 1)
#this dilation is used to increasae the thickness of the join or gap in between the image
# this itrations variable controls the thickness of the lines

eroded = cv2.erode(canny,kernal,iterations = 1)


cv2.imshow("Grey Image",gray)

cv2.imshow("Blur Image",blur)

cv2.imshow("Canny Image",canny)

cv2.imshow("Dilation Image",dilation)

cv2.imshow("Eroded Image",eroded)

cv2.waitKey(2)
cv2.destroyAllWindows
 
