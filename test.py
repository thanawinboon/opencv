#import numpy as np
import cv2
#import imutils
import numpy

try:
    im = cv2.imread('circles.jpg')

    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1.2, 100)

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = numpy.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(im, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(im, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('img', 800,800)
    cv2.imshow("output", numpy.hstack([im, output]))
    #cv2.imshow('img',myimage)
    cv2.waitKey(0)
finally:
    cv2.destroyAllWindows()
