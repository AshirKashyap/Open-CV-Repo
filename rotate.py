import numpy as nn
import cv2
import imutils
import argparse

argument = argparse.ArgumentParser()
argument.add_argument("-i", "--image", required = True, help = "pathway to the image")
args = vars(argument.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

(h, w) = image.shape[:2]
center = (h // 2, w // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotationimage = cv2.warpAffine(image, matrix, (h, w))
cv2.imshow("Rotated image", rotationimage)

cv2.waitKey(0)

matrix = cv2.getRotationMatrix2D(center, 90, -1.0)
rotatedimage = cv2.warpAffine(image, matrix, (h, w))
cv2.imshow("Rotated image", rotatedimage)

cv2.waitKey(0)

rotatedImage = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 degrees", rotatedImage)
cv2.waitKey(0)
