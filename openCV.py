import cv2
#import time

#img = cv2.imread("dog.png")
#new_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#new_img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
#gray = cv2.imread("dog.png",cv2.IMREAD_GRAYSCALE)

#new_img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#cv2.imshow(" blue dog img",new_img)#imshow() function alwaays take img in BGR
#cv2.imshow("Gray Dog img",gray)
#cv2.imshow("Dog img",img)


img2 = cv2.imread("download.png")

new_img = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)

gray = cv2.imread("download.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow(" RGB to BGR error img cat img",new_img)
cv2.imshow("Gray cat img",gray)
cv2.imshow("cat img",img2)

cv2.waitKey(0)

cv2.destroyAllWindows()