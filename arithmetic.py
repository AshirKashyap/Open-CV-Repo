from __future__ import print_function
import cv2
import argparse
import numpy as np


argument = argparse.ArgumentParser()
argument.add_argument("-i", "--image", required = True, help = "pathway to image")
args = vars(argument.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8 ([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8 ([100]))))
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

matrix = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, matrix)
cv2.imshow("Added", added)
matrix = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, matrix)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
