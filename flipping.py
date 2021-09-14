import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--image", required = True, help = "Pathway to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original image", image)

flipped = cv2.flip(image, 1)
cv2.imshow("flipped horizontally image", flipped)

cv2.waitKey(0)

flipped = cv2.flip(image, 0)
cv2.imshow("flipped vertically image", flipped)

cv2.waitKey(0)

flipped = cv2.flip(image, -1)
cv2.imshow("flipped horizontally and vertically image", flipped)

cv2.waitKey(0)
