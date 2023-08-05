import cv2

img = cv2.imread("C:/Users/Adit Kadiyan/Downloads/c116-openCv2-1-4--main/c116-openCv2-1-4--main/poster.jpg")

rocket = img[120:360,400:500]

img[0:240 ,500:600] = rocket

text_to_show = "I love coding at WhiteHatjr"

cv2.putText(img,
            text_to_show,
            (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(0,0,225)
            )

cv2.imshow("Image",img)

cv2.waitKey(0)