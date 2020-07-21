'''This is helpfull when you have a bunch of images and you want to run all of the
them again and again thus you can clip them and run alltogther '''

import cv2
import numpy as np
img =  cv2.imread("IM3.jpg")
imgHor = np.hstack((img,img))
imgVar = np.vstack((img,img))

cv2.imshow("Horizontal Image",imgHor)

cv2.imshow("Vertical Image",imgVar)
'''
here there are somw limitations with this function that is we can't resie o
the image that is there are 3 or 4 images all togther then they might go
out of frame as well
Second Thing is that both the images that we are joing shoud be of same scakle
i.e either bboth should be gray images or both should be colored images
then only this numpy feature of stacking will work properly '''
'''
     To stack the images togther and resize them all togther we need to us the
     Stack function '''


cv2.waitKey(1)
cv2.destroyAllWindows
