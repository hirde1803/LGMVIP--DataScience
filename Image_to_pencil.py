# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
#read image
Milo = cv2.imread("MILO.jpg")

#convert image to greyscale
gray_image = cv2.cvtColor(Milo, cv2.COLOR_BGR2GRAY)

#invert grayscale image
inverted = 200 - gray_image

#blur image using a gaussian point spread function
blurred = cv2.GaussianBlur(inverted, (19, 19), 0)

#invert blurred image
inverted_blurred = 200 - blurred


pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)


#show image
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)