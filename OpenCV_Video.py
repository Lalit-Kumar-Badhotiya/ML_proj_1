import cv2
#import time



cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if ret == False:
        continue
    cv2.imshow("pic",frame)

    key =cv2.waitKey(1)
    if key == ord("q"):
        break





























#img = cv2.imread("dog.png")
#new_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#new_img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
#gray = cv2.imread("dog.png",cv2.IMREAD_GRAYSCALE)

#new_img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img2 = cv2.imread("download.png")



#cv2.imshow(" blue dog img",new_img)#imshow() function alwaays take img in BGR
#cv2.imshow("Gray Dog img",gray)
#cv2.imshow("Dog img",img)



#cv2.waitKey(0)

cv2.destroyAllWindows()