import cv2

import numpy as np

img = cv2.imread("C://Users//User//Desktop//pratice//my1//Open CV//hardik.jpg")

print(img.shape)
resize = cv2.resize(img,(640,640))
#here in the above resize function the width came first followed by the height

cropped = img[0:500,600:750]
#here height came first then followed by the  width just opposite to that of resize function! be cautios here

cv2.imshow("Image",resize)
cv2.imshow("Cropped",cropped)
cv2.waitKey(1)
cv2.destroyAllWindows
