import cv2
import numpy as np

#Create a black Image
#Zero represents Black
blackImg=np.zeros([600,600])

#255 represents White
blackImg[200:400,200:400]=255

cv2.imshow("Black Image",blackImg)

cv2.waitKey(0)