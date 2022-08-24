from __future__ import print_function
import cv2
import numpy as np
import argparse
import random as rng
rng.seed(12345)


#def thresh_callback(val):
#    threshold = val

src = cv2.imread('shapes2.jpg')
src = cv2.resize(src, (1000, 750))
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

    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
   #  putting shape name at center of each shape
    if len(approx) == 3:
        cv2.putText(src, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
  
    elif len(approx) == 4:
        cv2.putText(src, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
  
    elif len(approx) == 5:
        cv2.putText(src, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
  
    elif len(approx) == 6:
        cv2.putText(src, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
  
 #   else:
  #      cv2.putText(src, 'circle', (x, y),
   #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#Draw contours
#rawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
#for i in range(len(contours)):
 #   color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
  #  cv2.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
    #Show in a window

#thresh_callback(thresh)
while True:
    try: 
        cv2.imshow('Edge', src)    
        # displaying the image after drawing contours      
        #cv2.imshow(source_window, src)
        cv2.waitKey(5000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        raise SystemExit