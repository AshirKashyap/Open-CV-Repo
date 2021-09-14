import cv2
import numpy as np
import imutils
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("--image", required = True, help = "Pathway to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original image", image)

ratio = 150.0 / image.shape[1]
dimensions = (150, int(image.shape[0] * ratio)) #converts the height by mult by the rotationimage

resizedImage = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized image (based on width)", resizedImage)

cv2.waitKey(0)

ratio = 50.0 / image.shape[0] #shape[0] = height, shape[1] = width
dimensions = (int(image.shape[1] * ratio), 50)

resizedImage = cv2.resize(image, dimensions, interpolation = cv2.INTER_AREA)
cv2.imshow("resized image (based on height)", resizedImage)

cv2.waitKey(0)


resizedImage = imutils.resize(image, width = 400)
cv2.imshow("resized image via imutils", resizedImage)

cv2.waitKey(0)
