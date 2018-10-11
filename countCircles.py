#imports computer vision version 2
import cv2

#import the numercial processing library for python, call it np for short
import numpy as np

imageName = 'coins.jpg'

try:
    #load an image from the disk
    circleImage = cv2.imread(imageName)
    
    #convert the image to grayscale
    grayImage = cv2.cvtColor(circleImage, cv2.COLOR_BGR2GRAY)
    
    #blur the image, so that similar colors get combined
    #https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
    grayImage = cv2.medianBlur(grayImage,5)

    #display the image that is greyscale and blurred.
    cv2.imshow('detected circles', circleImage)
    cv2.waitKey(0) #wait for the user to press a key

    #display the image that is greyscale and blurred.
    cv2.imshow('detected circles', grayImage)
    cv2.waitKey(0)

    """
    Detect circles in the image
    https://docs.opencv.org/3.1.0/da/d53/tutorial_py_houghcircles.html
    
    minDist: Minimum distance between the center (x, y) coordinates of detected circles.
    If the minDist is too small, multiple circles in the same neighborhood as the original
    may be (falsely) detected. If the minDist is too large, then some circles may not be
    detected at all.
    
    param1 will set the sensitivity; how strong the edges of the circles need to be.
    Too high and it won't detect anything, too low and it will find too much clutter.
    
    param2 will set how many edge points it needs to find to declare that it's found
    a circle. Again, too high will detect nothing, too low will declare anything to be
    a circle. The ideal value of param 2 will be related to the circumference of the circles.
    
    If you have an idea what size circles you are looking for, then it would be best to
    set min_radius and max_radius accordingly. Otherwise, it will return anything circular of any size.
    """
    circles = cv2.HoughCircles(grayImage, cv2.HOUGH_GRADIENT, 1, minDist=30, param1=10, param2=22, minRadius=10, maxRadius=100)

    circles = np.uint16(np.around(circles))

    #set a counter for the circles
    count = 0
    
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(circleImage,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(circleImage,(i[0],i[1]),2,(0,0,255),3)
        count = count + 1

    print("The number of circles found: ", count)
    
    #display the image with the circles highlighted.
    cv2.imshow('detected circles', circleImage)
    cv2.waitKey(0)
    
    #save the final image to disk
    cv2.imwrite('foundcircle.png', circleImage)


finally:
    cv2.destroyAllWindows()
