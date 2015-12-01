import numpy as np
import cv2

im =cv2.imread("260.jpg")
im2 = cv2.imread("300.jpg")
h = im.shape[0]                      
w = im.shape[1] 
im = cv2.resize(im,(w/4,h/4))
im2 =cv2.resize(im2,(w/4,h/4))
im = cv2.resize(im,(w/4,h/4))
imLab =cv2.cvtColor(im,cv2.COLOR_RGB2LAB)
imLab2 = cv2.cvtColor(im2,cv2.COLOR_RGB2LAB)
im_temp = np.zeros_like((im.shape[0],im.shape[1]),np.uint8)
im_temp2 = im_temp.copy()
#im_sample = imLab2 < 100
#print im_sample

im_temp = imLab[:,:,0]
im_temp2 = imLab2[:,:,0]
print im_temp
#imgray=cv2.calcBackProjectvtColor(im,cv2.COLOR_BGR2RGB)
cv2.imshow("",im_temp)
cv2.waitKey(0)
cv2.imshow("",im_temp2)
cv2.waitKey(0)
