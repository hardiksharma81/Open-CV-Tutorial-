import cv2

import numpy as np
 
img  = np.zeros((512,512,3),np.uint8)
print(img.shape)
img[:] = 255,0,0
'''
#here I'm using img[:] to color that black background
#this [:] is simillar as that in croping we can us it for cropping purpose as well
#see
# img[100:452,100:300]= 0,255,0
'''
#--------------------------------------------------------
#now we'll see how to draw a line
cv2.line(img,(0,0),(240,240),(0,255,0),3)# the 3 is used for the thickness of the line 

'''#cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)

#line(img_name, starting point , ending point , color)
'''
#drawing rectangle

cv2.rectangle(img,(0,0),(250,400),(0,0,255),cv2.FILLED)
'''filled is used insted of thickness
 to fill the entire inside part of the rectangle '''
#drawing Circle

cv2.circle(img,(250,250),212,(255,255,255),cv2.FILLED)
''' Here (250,250) is the location of our center
    212 is the radius of the circle
    255,255,255 is colour palet you can change it as per your likings'''
#putting fornt on canvas

cv2.putText(img,"HARDIK",(80,250),cv2.FONT_HERSHEY_COMPLEX,3,(10,240,0),1)
'''
here HARDIK is the text that we wish to show on the canvas
    190,250 is the locantion on the canvas where i want to put it
    cv2.FONT is the forn tof the text
    1 is the scale of the font i.e ye kitna bada dikhega humey on the canvas it can be float value as well
    (10,240,0) is the color pallet of your chosen font
    1 is the thickness of the font '''


cv2.imshow("image",img)
#this will create  a blank background image for us 
cv2.waitKey(0)
