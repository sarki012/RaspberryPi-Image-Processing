import cv2
import numpy as np

image = cv2.imread('waterBottle.jpg')
width, height, channels = image.shape
print (height, width, channels)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

for x in range(0, (width - 1)):
    for y in range(0, (height - 1)):
        (b, g, r) = image[x,y]
        # if b > 220 & g > 220 & r > 220:
        image[x, y] = (0, 0, 255)
        #(b, g, r) = image[x, y]
while True:
    try:       
        cv2.imshow('image', image)
        cv2.waitKey(5000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        raise SystemExit

