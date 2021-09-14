import cv2
import numpy as n
import argparse
import imutils

argument = argparse.ArgumentParser()
argument.add_argument("-i", "--image", required = True, help = "pathway to image")
args = vars(argument.parse_args())

picture = cv2.imread(args["image"])
cv2.imshow("Original Image", picture)

matrix = n.float32([[1, 0, 25], [0, 1, 50]])
shift = cv2.warpAffine(picture, matrix, (picture.shape[1], picture.shape[0]))
cv2.imshow("Shifted down and right", shift)

matrix = n.float32([[1, 0, -50], [0, 1, -90]])
shift = cv2.warpAffine(picture, matrix, (picture.shape[1], picture.shape[0]))
cv2.imshow("Shift up and left", shift)
cv2.waitKey(0)

shift = imutils.translate(picture, 0, 100)
cv2.imshow("Shifted Downwards", shift)
cv2.waitKey(0)
