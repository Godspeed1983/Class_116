import cv2

#Read image
img=cv2.imread("C:/Users/Adit Kadiyan/Downloads/c116-openCv2-1-4--main/c116-openCv2-1-4--main/butterfly.jpg")

#Display colored image
cv2.imshow("Colorful_butterfly",img)

#Convert colored image into grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("GrayScale_Image",gray_img)


cv2.waitKey(0)