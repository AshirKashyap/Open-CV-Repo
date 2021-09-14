import cv2
import argparse
import numpy as np

argument = argparse.ArgumentParser()
argument.add_argument("-i", "--image", required = True, help = "pathway to image")
args = vars(argument.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

cv2.waitKey(0)

cropped = image[30:120, 240:335]
cv2.imshow("Trex Face image", cropped)

cv2.waitKey(0)
