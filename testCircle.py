import cv2
#import imutils
import numpy as np

try:
    img = cv2.imread('coins.jpg',0)
    img = cv2.medianBlur(img,5)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

    cimg = cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=20,param2=40,minRadius=80,maxRadius=100)

    circles = np.uint16(np.around(circles))

    count = 0
    
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        count = count + 1

    print(count)
    cv2.imshow('detected circles',cimg)
    
    px = cimg[100,100]
    
#    ball = img[550:340, 330:390]
 #   img[550:333, 100:160] = ball
    print(px)
    
    cv2.waitKey(0)
    
    cv2.imwrite('foundcircle.png',cimg)


finally:
    cv2.destroyAllWindows()
