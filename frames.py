import cv2
import numpy as np
import argparse
#import random as rng
#rng.seed(12345)

vidcap = cv2.VideoCapture('shape.h264')
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite('frame%d.jpg' % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
count2 = 0
while True:
    try:
        #src = cv2.imread('frame%d.jpg' % count2)
        src = cv2.imread('frame40.jpg')
        src = cv2.resize(src, (1000, 750))
        cv2.imshow('Image', src)    
        count2 += 1
        if count2 > 94:
            count2 = 0
        if src is None:
            print('Could not open or find the image:', args.input)
            exit(0)
        # Convert image to gray and blur it
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src_gray = cv2.blur(src_gray, (3,3))

        # Create Window
        #source_window = 'Source'
        #cv2.namedWindow(source_window)
        max_thresh = 255
        thresh = 100 # initial threshold
        #_, threshold = cv2.threshold(src_gray, 200, 255, cv2.THRESH_BINARY)
        #cv2.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
        #Detect edges using Canny
        #canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
        canny_output = cv2.Canny(src_gray, 50, 150)
            #Find contours
        #_, contours, hierarchy = cv2.findContours(
        #   canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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
        
            # cv2.approxPloyDP() function to approximate the shape
            approx = cv2.approxPolyDP(
                contour, 0.01 * cv2.arcLength(contour, True), True)
            
            # using drawContours() function
            cv2.drawContours(src, [contour], -1, (0, 0, 255), 20)
            cv2.imshow('Edge', src)    
            # displaying the image after drawing contours      
            #cv2.imshow(source_window, src)
            #cv2.waitKey(5000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        raise SystemExit