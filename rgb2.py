import cv2
import numpy as np

image = cv2.imread('calculator.jpg')


(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

resizedImage = cv2.resize(image, (1000, 750))
width, height, channels = resizedImage.shape
print (height, width, channels)
for x in range(0, (width - 1)):
    for y in range(0, (height - 1)):
        (b, g, r) = resizedImage[x,y]
        if b < 75:
            if g < 75:
                if r < 75:
                    resizedImage[x, y] = (255, 0, 0)
while True:
    try:       
        cv2.imshow('image', resizedImage)
        cv2.waitKey(5000)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        raise SystemExit

