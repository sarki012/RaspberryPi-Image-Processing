import cv2
import numpy as np
import argparse
count2 = 0
while True:
    try:
        src = cv2.imread('frame%d.jpg' % count2)
        #src = cv2.imread("frame40.jpg")
        src = cv2.resize(src, (1000, 750))
        count2 += 1
        if count2 > 94:
            count2 = 0    
        # Convert image to gray and blur it
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src_gray = cv2.blur(src_gray, (3,3))
        canny_output = cv2.Canny(src_gray, 50, 150)
        contours, _ = cv2.findContours(
        canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
        i = 0
        #using drawContours() function
        # list for storing names of shapes
        for contour in contours:
            # here we are ignoring first counter because 
            # findcontour function detects whole image as shape
            if i == 0:
                i = 1
                continue            
            # using drawContours() function
            cv2.drawContours(src, [contour], -1, (0, 0, 255), 20)
            M = cv2.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
        cv2.imshow('Image', src) 
        cv2.waitKey(10)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        raise SystemExit