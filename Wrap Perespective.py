'''
here we'll learn about how to cut-out a particular piece from the picture
to do so we'll be needing two libraryes
i.e open cv and numpy
'''



import cv2
import numpy as np
img = cv2.imread("card.jpg")

width,height = 250,350
#self assumed
#usually cards are madeup of thses lengths only


pts1 = np.float32([[150,21],[254,20],[103,171],[210,196]])

#here we are finding the coordinates that we'll be using to crop the image
# we can easily find the coordinated usinng paint



pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1,pts2)

'''
    converting the points that we have collected from the image into the perspective transform
    '''
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)

cv2.imshow("Wrapped Image",imgOutput)
cv2.waitKey(1)
cv2.destroyAllWindows
