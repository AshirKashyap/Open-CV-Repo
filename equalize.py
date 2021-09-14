import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--image", required = True,
help = "Pathway to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalize = cv2.equalizeHist(image)

cv2.imshow("Hist Equi", np.hstack([image, equalize]))
cv2.waitKey(0)
